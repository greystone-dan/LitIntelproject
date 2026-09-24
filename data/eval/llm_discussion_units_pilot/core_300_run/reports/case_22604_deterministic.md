# Discussion Units: case 22604

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **33**
- Continuity pairs: **32**
- Discussion Units: **3**
- Paragraph source hashes: **33**
- Sub-themes: **9**

## 22604:1 · paragraphs 0-29

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `f45644996623ee31c194ac0043f57d01e2f1bdaac52fae389ca364d344efc13d`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22604:1:subtheme:1 · paragraphs 0-1

- Raw key terms: `decision, immigration, applicant, application, april, batres, board, brought`
- Display key terms: `april, batres, brought`
- Argument roles: `governing_rule, party_position`
- Explanation: Observed roles: governing_rule, party_position Display terms: april, batres, brought Position/evidence statements: The applicant, a citizen of El Salvador, claims a well-founded fear of persecution as a victim of a criminal street gang. Rule/authority context: [1] This is an application brought by the applicant pursuant to s. Evidence spans paragraphs 0-1. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `party_position` cue `claims` at chunk `5060412` offsets `317-323`; context: The applicant, a citizen of El Salvador, claims a well-founded fear of persecution as a victim of a criminal street gang.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5060412` offsets `52-63`; context: [1] This is an application brought by the applicant pursuant to s.

#### 22604:1:subtheme:2 · paragraphs 2-9

- Raw key terms: `applicant, salvador, gang, board, protection, family, members, parents`
- Display key terms: `salvador, gang, protection, family, members, parents`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, party_position, reasoning_application Display terms: salvador, gang, protection, family, members, parents Position/evidence statements: [3] The applicant, a twenty-year old female citizen of El Salvador, claims a risk to her life at the hands of criminal street gangs in El Salvador. Rule/authority context: [7] The Board determined that the applicant was neither a Convention refugee nor a person in need of protection pursuant to sections 96 and 97 of the IRPA. Application context: She mentioned that in any event, the police would not be able to protect her in El Salvador because they lack the personnel and resources. Evidence spans paragraphs 2-9. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `found that` at chunk `5060413` offsets `14-24`; context: [2] The Board found that the applicant had not rebutted the presumption that adequate state protection exists in El Salvador, and that the applicant had a reasonable internal flight alternative in San Salvador.
- Evidence: `party_position` cue `claims` at chunk `5060414` offsets `68-74`; context: [3] The applicant, a twenty-year old female citizen of El Salvador, claims a risk to her life at the hands of criminal street gangs in El Salvador.
- Evidence: `counterargument_limitation` cue `but` at chunk `5060414` offsets `303-306`; context: The alleged that in 2001, unknown criminals believed to be part of a street gang called the Mara Salvatrucha targeted her family and asked them for money, but were refused by her parents.
- Evidence: `reasoning_application` cue `because` at chunk `5060416` offsets `205-212`; context: She mentioned that in any event, the police would not be able to protect her in El Salvador because they lack the personnel and resources.
- Evidence: `evidence_fact` cue `determined that` at chunk `5060418` offsets `14-29`; context: [7] The Board determined that the applicant was neither a Convention refugee nor a person in need of protection pursuant to sections 96 and 97 of the IRPA.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5060418` offsets `112-123`; context: [7] The Board determined that the applicant was neither a Convention refugee nor a person in need of protection pursuant to sections 96 and 97 of the IRPA.
- Evidence: `evidence_fact` cue `found that` at chunk `5060419` offsets `21-31`; context: [8] First, the Board found that the applicant had not rebutted the presumption of state protection with evidence of a clear and convincing nature.
- Evidence: `evidence_fact` cue `evidence` at chunk `5060420` offsets `257-265`; context: [9] The Board recognized that gangs remained a problem in El Salvador and that membership in gangs and gang violence had increased; nevertheless, it concluded that the applicant had not rebutted the presumption of state protection with clear and convincing evidence establishing that the state would be unable or unwilling to protect the applicant should she require protection upon her return to El Salvador.
- Evidence: `counterargument_limitation` cue `nevertheless` at chunk `5060420` offsets `132-144`; context: [9] The Board recognized that gangs remained a problem in El Salvador and that membership in gangs and gang violence had increased; nevertheless, it concluded that the applicant had not rebutted the presumption of state protection with clear and convincing evidence establishing that the state would be unable or unwilling to protect the applicant should she require protection upon her return to El Salvador.

#### 22604:1:subtheme:3 · paragraphs 10-12

- Raw key terms: `applicant, board, evidence, finding, issues, mara, parents, protection`
- Display key terms: `finding, issues, mara, parents, protection`
- Argument roles: `evidence_fact, governing_rule, issue, party_position`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, party_position Display terms: finding, issues, mara, parents, protection Position/evidence statements: First, he argued that the Board failed to take account of the totality of the evidence in determining that there is state protection for the applicant, and disregarded the applicant’s explanation as to why her parents di Rule/authority context: New Brunswick, 2008 SCC 9, the weight of the jurisprudence had established that overall, the standard of review of a state protection finding should be reasonableness: see, for ex. Evidence spans paragraphs 10-12. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `ISSUES` at chunk `5060421` offsets `544-550`; context: ISSUES
- Evidence: `evidence_fact` cue `found that` at chunk `5060421` offsets `20-30`; context: [10] The Board also found that the applicant had a reasonable internal flight alternative (“IFA”) in Sal Salvador and that while her parents had experienced several incidents of violence while living there, there was insufficient evidence to connect these incidents to the previous ones, or to establish that those incidents were anything more than random criminal acts.
- Evidence: `issue` cue `issues` at chunk `5060422` offsets `44-50`; context: [11] Counsel for the applicant raised three issues in her written and oral arguments.
- Evidence: `party_position` cue `argued` at chunk `5060422` offsets `96-102`; context: First, he argued that the Board failed to take account of the totality of the evidence in determining that there is state protection for the applicant, and disregarded the applicant’s explanation as to why her parents did not seek state protection.
- Evidence: `evidence_fact` cue `evidence` at chunk `5060422` offsets `164-172`; context: First, he argued that the Board failed to take account of the totality of the evidence in determining that there is state protection for the applicant, and disregarded the applicant’s explanation as to why her parents did not seek state protection.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `5060423` offsets `220-233`; context: New Brunswick, 2008 SCC 9, the weight of the jurisprudence had established that overall, the standard of review of a state protection finding should be reasonableness: see, for ex.

#### 22604:1:subtheme:4 · paragraphs 13-14

- Raw key terms: `canada, citizenship, clearly, dunsmuir, fact, immigration, minister, reasonableness`
- Display key terms: `clearly, dunsmuir, fact, reasonableness`
- Argument roles: `governing_rule, issue, reasoning_application`
- Explanation: Observed roles: governing_rule, issue, reasoning_application Display terms: clearly, dunsmuir, fact, reasonableness Rule/authority context: The two-pronged test for determining whether an IFA exists clearly calls for the reasonableness standard, since findings of fact have to be assessed against a legal test. Application context: It is therefore not surprising to find that the cases decided post Dunsmuir have continued to be based on the standard of reasonableness: Samuel v. Evidence spans paragraphs 13-14. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5060424` offsets `111-119`; context: The question as to whether there is clear and convincing confirmation of a state’s inability to protect is clearly a question of mixed fact and law, and as such it attracts the application of the reasonableness standard: Pacasum v.
- Evidence: `issue` cue `issues` at chunk `5060425` offsets `38-44`; context: [14] The same is true with respect to issues pertaining to an IFA.
- Evidence: `governing_rule` cue `legal test` at chunk `5060425` offsets `226-236`; context: The two-pronged test for determining whether an IFA exists clearly calls for the reasonableness standard, since findings of fact have to be assessed against a legal test.
- Evidence: `reasoning_application` cue `therefore` at chunk `5060425` offsets `244-253`; context: It is therefore not surprising to find that the cases decided post Dunsmuir have continued to be based on the standard of reasonableness: Samuel v.

#### 22604:1:subtheme:5 · paragraphs 15-19

- Raw key terms: `protection, state, canada, case, immigration, minister, applicant, citizenship`
- Display key terms: `protection, state, case`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position, reasoning_application Display terms: protection, state, case Position/evidence statements: [16] The applicant has submitted that in deciding the issue of state protection, the Board must consider whether protection was effective, and whether the efforts underway to counter gang violence were applied at the ope Application context: [16] The applicant has submitted that in deciding the issue of state protection, the Board must consider whether protection was effective, and whether the efforts underway to counter gang violence were applied at the ope | The test is not met merely because the applicants are able to demonstrate that the state cannot provide perfect protection. Evidence spans paragraphs 15-19. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5060426` offsets `171-178`; context: It is also concerned with whether the decision falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and the law.
- Evidence: `issue` cue `issue` at chunk `5060427` offsets `54-59`; context: [16] The applicant has submitted that in deciding the issue of state protection, the Board must consider whether protection was effective, and whether the efforts underway to counter gang violence were applied at the operational level.
- Evidence: `party_position` cue `submitted` at chunk `5060427` offsets `23-32`; context: [16] The applicant has submitted that in deciding the issue of state protection, the Board must consider whether protection was effective, and whether the efforts underway to counter gang violence were applied at the operational level.
- Evidence: `reasoning_application` cue `applied` at chunk `5060427` offsets `202-209`; context: [16] The applicant has submitted that in deciding the issue of state protection, the Board must consider whether protection was effective, and whether the efforts underway to counter gang violence were applied at the operational level.
- Evidence: `evidence_fact` cue `determined that` at chunk `5060428` offsets `105-120`; context: Justice LaForest determined that courts must presume that a state is capable of protecting its citizens.
- Evidence: `reasoning_application` cue `because` at chunk `5060428` offsets `540-547`; context: The test is not met merely because the applicants are able to demonstrate that the state cannot provide perfect protection.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `5060428` offsets `602-608`; context: The test is not met merely because the applicants are able to demonstrate that the state cannot provide perfect protection.
- Evidence: `evidence_fact` cue `evidence` at chunk `5060429` offsets `461-469`; context: In that last case, the Court insisted that the applicant bears both an evidentiary and legal burden; he or she must introduce evidence of inadequate state protection, and must convince the trier of fact on a balance of probabilities that the evidence adduced establishes that the state protection is inadequate.
- Evidence: `counterargument_limitation` cue `but` at chunk `5060429` offsets `705-708`; context: Moreover, the evidence does not only have to be reliable, but it must also have sufficient probative value to meet the applicable standard of proof.

#### 22604:1:subtheme:6 · paragraphs 20-27

- Raw key terms: `evidence, protection, applicant, board, state, always, adequate, argued`
- Display key terms: `protection, state, always, adequate`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position, reasoning_application Display terms: protection, state, always, adequate Position/evidence statements: [9] The applicants contend, nonetheless, that it remains an error for an RPD panel to fail to consider whether the measures it deems adequate are at least minimally effective. | [20] Pointing to some items of the documentary evidence indicating that the efforts of the State have not always been crowned with success, the applicant argued that the Board had selective regard for the evidence before Application context: In fact, I find the context of this case to be materially indistinguishable from those canvassed by my colleague Justice Robert Barnes in Paniagua v. | The applicant argued that they did not seek protection because of their fear of reprisal by the Mara Salvatrucha. Evidence spans paragraphs 20-27. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5060431` offsets `103-110`; context: [9] The applicants contend, nonetheless, that it remains an error for an RPD panel to fail to consider whether the measures it deems adequate are at least minimally effective.
- Evidence: `party_position` cue `contend` at chunk `5060431` offsets `19-26`; context: [9] The applicants contend, nonetheless, that it remains an error for an RPD panel to fail to consider whether the measures it deems adequate are at least minimally effective.
- Evidence: `evidence_fact` cue `evidence` at chunk `5060432` offsets `517-525`; context: When that state is a democratic society, such as Mexico, albeit one facing significant challenges with corruption and other criminality, the quality of the evidence necessary to rebut the presumption will be higher.
- Evidence: `party_position` cue `argued` at chunk `5060434` offsets `154-160`; context: [20] Pointing to some items of the documentary evidence indicating that the efforts of the State have not always been crowned with success, the applicant argued that the Board had selective regard for the evidence before it and failed to appreciate the extent of the Mara phenomenon.
- Evidence: `evidence_fact` cue `evidence` at chunk `5060434` offsets `47-55`; context: [20] Pointing to some items of the documentary evidence indicating that the efforts of the State have not always been crowned with success, the applicant argued that the Board had selective regard for the evidence before it and failed to appreciate the extent of the Mara phenomenon.
- Evidence: `reasoning_application` cue `I find` at chunk `5060434` offsets `504-510`; context: In fact, I find the context of this case to be materially indistinguishable from those canvassed by my colleague Justice Robert Barnes in Paniagua v.
- Evidence: `counterargument_limitation` cue `But` at chunk `5060434` offsets `284-287`; context: But a careful reading of the Board’s reasons reveals that the Board was cognizant of the evidence detailing the persistent problem of gang violence in El Salvador, and acknowledged it explicitly in its reasons.
- Evidence: `evidence_fact` cue `evidence` at chunk `5060435` offsets `55-63`; context: [21] The fact that the Board did not deal with all the evidence submitted by the applicant does not establish that it was ignored.
- Evidence: `party_position` cue `argued` at chunk `5060436` offsets `429-435`; context: The applicant argued that they did not seek protection because of their fear of reprisal by the Mara Salvatrucha.
- Evidence: `evidence_fact` cue `record` at chunk `5060436` offsets `285-291`; context: While the Board noted that the applicant herself, who was a minor at the time, did not have a duty to seek protection before fleeing, the record shows there was no reasonable explanation for the family’s failure to report the gang threats and incidents to the police.
- Evidence: `reasoning_application` cue `because` at chunk `5060436` offsets `470-477`; context: The applicant argued that they did not seek protection because of their fear of reprisal by the Mara Salvatrucha.
- Evidence: `evidence_fact` cue `found that` at chunk `5060437` offsets `127-137`; context: The Board, however, went further and found that the applicant had an internal flight alternative in San Salvador.
- Evidence: `counterargument_limitation` cue `however` at chunk `5060437` offsets `101-108`; context: The Board, however, went further and found that the applicant had an internal flight alternative in San Salvador.
- Evidence: `party_position` cue `argued` at chunk `5060438` offsets `302-308`; context: The applicant argued that she was at risk not simply as a potential victim of crime, but as a young woman.
- Evidence: `evidence_fact` cue `evidence` at chunk `5060438` offsets `154-162`; context: There was insufficient evidence on the record to establish that the applicant faced a personalized risk to her life at the hands of Salvadoran street gangs.
- Evidence: `reasoning_application` cue `because` at chunk `5060438` offsets `514-521`; context: At the hearing, counsel for the applicant contended that all Salvadoran aged 16 to 40 would have a valid refugee claim because of the risk created by the Maras.
- Evidence: `counterargument_limitation` cue `but` at chunk `5060438` offsets `373-376`; context: The applicant argued that she was at risk not simply as a potential victim of crime, but as a young woman.

#### 22604:1:subtheme:7 · paragraphs 28-29

- Raw key terms: `reasons, applicant, application, best, board, category, certification, certified`
- Display key terms: `best, category, certification, certified`
- Argument roles: `disposition, evidence_fact, governing_rule, issue`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, issue Display terms: best, category, certification, certified Rule/authority context: Pursuant to s. Operative outcome context: [26] For all the foregoing reasons, this application for judicial review is dismissed. Evidence spans paragraphs 28-29. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5060439` offsets `632-637`; context: As a result, the Board made no error in failing to consider this issue specifically in its reasons.
- Evidence: `evidence_fact` cue `evidence` at chunk `5060439` offsets `30-38`; context: [25] At best, the documentary evidence establishes that all Salvadorans face a generalized risk of violence from gangs.
- Evidence: `governing_rule` cue `Pursuant to` at chunk `5060439` offsets `120-131`; context: Pursuant to s.
- Evidence: `disposition` cue `dismissed` at chunk `5060440` offsets `76-85`; context: [26] For all the foregoing reasons, this application for judicial review is dismissed.

#### Section text

Velasquez v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2009-02-02
Neutral citation
2009 FC 109
File numbers
IMM-2299-08
Decision Content
Date: 20090202
Docket: IMM-2299-08
Citation: 2009 FC 109
OTTAWA, ONTARIO, FEBRUARY 02, 2009
PRESENT: The Honourable Mr. Justice de Montigny
BETWEEN:
VENTURA SARAI BATRES VELASQUEZ
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
REASONS FOR ORDER AND ORDER

[1] This is an application brought by the applicant pursuant to s. 72 of the Immigration and Refugee Protection Act, S.C. 2001, c. 27 for judicial review of a decision of the Refugee Protection Division of the Immigration and Refugee Board (the “Board”) dated April 28, 2008. The applicant, a citizen of El Salvador, claims a well-founded fear of persecution as a victim of a criminal street gang.

[2] The Board found that the applicant had not rebutted the presumption that adequate state protection exists in El Salvador, and that the applicant had a reasonable internal flight alternative in San Salvador. It is from these findings that this application for judicial review arises.
BACKGROUND

[3] The applicant, a twenty-year old female citizen of El Salvador, claims a risk to her life at the hands of criminal street gangs in El Salvador. The alleged that in 2001, unknown criminals believed to be part of a street gang called the Mara Salvatrucha targeted her family and asked them for money, but were refused by her parents. The applicant also alleges that the gang members later attempted to enter her parents’ home, but were unsuccessful. Shots were fired in the attempt, and the criminals threatened to return. Subsequently, the applicant’s family moved to San Salvador.

[4] The applicant also testified that while in San Salvador, her parents were robbed at knife point on one occasion by a group of gang members, and that a man attacked her with a knife once while in a supermarket and stole her necklace.

[5] The applicant added that her family never reported any of the incidents to the police for fear of reprisals. She mentioned that in any event, the police would not be able to protect her in El Salvador because they lack the personnel and resources. The applicant also testified that gang violence is increasing every day in El Salvador.

[6] The applicant and her family remained in San Salvador until 2004, when the applicant’s parents sent her to the United States. She remained there illegally until March 2006, when she travelled to Canada and made a refugee claim at the border crossing.
THE IMPUGNED DECISION

[7] The Board determined that the applicant was neither a Convention refugee nor a person in need of protection pursuant to sections 96 and 97 of the IRPA.

[8] First, the Board found that the applicant had not rebutted the presumption of state protection with evidence of a clear and convincing nature. Reviewing the documentary evidence, the Board stated that El Salvador is a democracy with the civilian National Police Force maintaining public security, and the Ministry of Defence providing national security. Moreover, there are various offices to deal with allegations and complaints of corruption within the police force. Referring to the 2007 U.S. Department of State Report, the Board indicated that the government is making serious efforts in combating gang violence by establishing an Anti-Gang Taskforce, headed by the Ministry of Public Security, which successfully arrested almost 6 000 current and former gang members and are making serious efforts in combating gang violence.

[9] The Board recognized that gangs remained a problem in El Salvador and that membership in gangs and gang violence had increased; nevertheless, it concluded that the applicant had not rebutted the presumption of state protection with clear and convincing evidence establishing that the state would be unable or unwilling to protect the applicant should she require protection upon her return to El Salvador.

[10] The Board also found that the applicant had a reasonable internal flight alternative (“IFA”) in Sal Salvador and that while her parents had experienced several incidents of violence while living there, there was insufficient evidence to connect these incidents to the previous ones, or to establish that those incidents were anything more than random criminal acts. The Board also noted that the applicant’s parents continue to live in San Salvador, and that there is no evidence that they continue to be targeted by the Mara Salvatrucha.
ISSUES

[11] Counsel for the applicant raised three issues in her written and oral arguments. First, he argued that the Board failed to take account of the totality of the evidence in determining that there is state protection for the applicant, and disregarded the applicant’s explanation as to why her parents did not seek state protection. Second, he submitted that the Board failed to take into account the applicant’s evidence as to the risk she faces as a young woman from street gangs in finding that she has an IFA in San Salvador. Finally, he contended that the Board failed to undertake a separate s. 97 analysis as to the objective risk the applicant as a young woman faces from the Mara Salvatrucha or other gangs in El Salvador.
ANALYSIS

[12] Findings of fact by a specialized administrative tribunal are entitled to great deference by a reviewing court. Prior to the decision of the Supreme Court in Dunsmuir v. New Brunswick, 2008 SCC 9, the weight of the jurisprudence had established that overall, the standard of review of a state protection finding should be reasonableness: see, for ex., Chaves v. Canada (Minister of Citizenship and Immigration), 2005 FC 193; Franklyn v. Canada (Minister of Citizenship and Immigration), 2005 FC 1249; Hinzman v. Canada (Minister of Citizenship and Immigration), 2007 FCA 171. The same was true of an IFA finding: see Ali v. Canada (Minister of Citizenship and Immigration), 2001 FCT 193; Chorny v. Canada (Minister of Citizenship and Immigration), 2003 FC 999.

[13] Several decisions of this Court have confirmed that Dunsmuir has not changed the law in this respect. The question as to whether there is clear and convincing confirmation of a state’s inability to protect is clearly a question of mixed fact and law, and as such it attracts the application of the reasonableness standard: Pacasum v. Canada (Minister of Citizenship and Immigration), 2008 FC 822; Rodriguez Estrella v. Canada (Citizenship and Immigration), 2008 FC 633; Eler v. Canada (Minister of Citizenship and Immigration), 2008 FC 334.

[14] The same is true with respect to issues pertaining to an IFA. The two-pronged test for determining whether an IFA exists clearly calls for the reasonableness standard, since findings of fact have to be assessed against a legal test. It is therefore not surprising to find that the cases decided post Dunsmuir have continued to be based on the standard of reasonableness: Samuel v. Canada (Minister of Citizenship and Immigration), 2008 FC 762; Khokhar v. Canada (Minister of Citizenship and Immigration), 2008 FC 449; Aguilar v. Canada (Minister of Citizenship and Immigration), 2008 FC 1180.

[15] Reasonableness is generally concerned with the existence of justification, transparency and intelligibility in the decision-making process. It is also concerned with whether the decision falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and the law. The move towards a single reasonableness standard does not pave the way for a more intrusive review by courts. Indeed, paragraph 18.1(4)(d) of the Federal Courts Act, R.S.C. 1985, c. F-7 makes it clear that findings of fact should be disturbed only if they are made in a perverse or capricious manner or without regard for the material before the tribunal.

[16] The applicant has submitted that in deciding the issue of state protection, the Board must consider whether protection was effective, and whether the efforts underway to counter gang violence were applied at the operational level. This argument is flawed, unsupported by the case law, and rests on a false premise.

[17] In the seminal case of Canada (Attorney General) v. Ward, [1993] 2 S.C.R. 689, Mr. Justice LaForest determined that courts must presume that a state is capable of protecting its citizens. He made it clear that the underlying rationale for that presumption is that international protection comes into play as a surrogate, when no alternative remains to the claimant. For this presumption to be displaced, the claimant must provide clear and convincing evidence of the state’s inability to protect him or her. The test is not met merely because the applicants are able to demonstrate that the state cannot provide perfect protection. No government can guarantee the protection of all of its citizens at all times: Canada (Minister of Employment and Immigration) v. Villafranca (1992), 99 D.L.R.(4th) 334, at p. 337 (F.C.A.).

[18] The Federal Court of Appeal has recently addressed the burden of proof and the standard of proof required to rebut the presumption of state protection, first in Hinzman v. Canada (Minister of Citizenship and Immigration), 2007 FCA 171, and subsequently in Canada (Minister of Citizenship and Immigration) v. Carillo, 2008 FCA 94. In that last case, the Court insisted that the applicant bears both an evidentiary and legal burden; he or she must introduce evidence of inadequate state protection, and must convince the trier of fact on a balance of probabilities that the evidence adduced establishes that the state protection is inadequate. Moreover, the evidence does not only have to be reliable, but it must also have sufficient probative value to meet the applicable standard of proof.

[19] My colleague Justice Mosley aptly summarized the state of the law with respect to state protection in Flores v. Canada (Minister of Citizenship and Immigration), 2008 FC 723:

[9] The applicants contend, nonetheless, that it remains an error for an RPD panel to fail to consider whether the measures it deems adequate are at least minimally effective.

[10] While this is an attractive argument, it does not convey the current state of the law in Canada in my view. As noted by the Federal Court of Appeal in Carillo, the decision of the Supreme Court of Canada in Canada (Attorney General) v. Ward, [1993] 2 S.C.R. 689 stressed that refugee protection is a surrogate for the protection of a claimant’s own state. When that state is a democratic society, such as Mexico, albeit one facing significant challenges with corruption and other criminality, the quality of the evidence necessary to rebut the presumption will be higher. It is not enough for a claimant merely to show that his government has not always been effective at protecting persons in his particular situation: Canada (Minister of Employment and Immigration) v. Villafranca (1992), 18 Imm. L.R.(2d) 130 (F.C.A.).

[11] The serious efforts to provide protection noted by the panel member support the presumption set out in Ward. Requiring effectiveness of other countries’ authorities would be to ask of them what our own country is not always able to provide.

[20] Pointing to some items of the documentary evidence indicating that the efforts of the State have not always been crowned with success, the applicant argued that the Board had selective regard for the evidence before it and failed to appreciate the extent of the Mara phenomenon. But a careful reading of the Board’s reasons reveals that the Board was cognizant of the evidence detailing the persistent problem of gang violence in El Salvador, and acknowledged it explicitly in its reasons. In fact, I find the context of this case to be materially indistinguishable from those canvassed by my colleague Justice Robert Barnes in Paniagua v. Canada (Minister of Citizenship and Immigration), 2008 FC 1350, and I make mine his comments:
7. The Board decision acknowledged the seriousness of the gang problem in El Salvador and the very high crime and murder rates associated with that activity. Clearly the Board was aware of the problems with gang related law enforcement in El Salvador.
8. I do not agree that the failure by the Board to specifically refer to all documentary evidence dealing with the gravity of the problem of gang violence in El Salvador constitutes a reviewable error. The Board understood that state protection in El Salvador was not perfect but it also recognized correctly that perfection is not the standard by which the sufficiency of protection is to be measured. The Board identified several state initiatives directed at combating gang activity; indeed some of the country condition reports relied upon by Mr. Rauda Paniagua speak directly to the effectiveness, in part, of the government’s “tough” anti-gang reforms. Against this evidentiary record it was open to the Board to be very concerned that Mr. Rauda Paniagua had made no effort to seek state protection before coming to Canada. Although the problems of gang violence in El Salvador were unquestionably profound, there was plausible evidence that the state protection apparatus in that country continued to function. It is not for the Court to reweigh the evidence or to substitute its views of that evidence for those of the Board. While a different conclusion could have been reached on this evidence, I am not satisfied that the Board’s treatment of the state protection evidence or the conclusions it reached were unreasonable.
See also: Ayala v. Canada (Minister of Citizenship and Immigration), 2007 FC 690

[21] The fact that the Board did not deal with all the evidence submitted by the applicant does not establish that it was ignored. In fact, some of it was irrelevant, and some was outdated. Again, the Court was not blind to the rise of street gangs in El Salvador and to the challenges this phenomenon poses for the police forces. But having weighed the evidence in its totality, it came to the conclusion that state protection was available and adequate. I have not been persuaded that this assessment is unreasonable.

[22] It is always problematic for an applicant to rebut the presumption of state protection when no attempt has been made to seek that protection. While the Board noted that the applicant herself, who was a minor at the time, did not have a duty to seek protection before fleeing, the record shows there was no reasonable explanation for the family’s failure to report the gang threats and incidents to the police. The applicant argued that they did not seek protection because of their fear of reprisal by the Mara Salvatrucha. But that cannot be sufficient, in and of itself. Once again, the Board looked at the evidence and determined that protection for similarly situated persons would be adequate. In particular, the Board looked at the various measures taken by the government and found that the authorities were making serious efforts, with some measure of success, to contain the increased crime rates due to increased membership in the Mara Salvatrucha and other gangs. It also noted that accusations can be filed anonymously by the victim or another person. In light of the evidence before it, the Board could reasonably concluded that there was no reasonable explanation for not even reporting once the threats and thefts ton which they were subjected.

[23] This finding of state protection was sufficient to dispose of the applicant’s claim. The Board, however, went further and found that the applicant had an internal flight alternative in San Salvador. The Board determined that there was insufficient evidence to establish the existence of any risk to the applicant in San Salvador, owing to the fact that the criminal incidents experienced by her family there were not established to have been connected to the Mara Salvatrucha gand, and due to the fact that her family has lived peacefully there ever since. These were also reasonable findings.

[24] Finally, the applicant’s argument that the Board erred when it failed to conduct a separate section 97 analysis is unfounded. There was insufficient evidence on the record to establish that the applicant faced a personalized risk to her life at the hands of Salvadoran street gangs. The applicant argued that she was at risk not simply as a potential victim of crime, but as a young woman. At the hearing, counsel for the applicant contended that all Salvadoran aged 16 to 40 would have a valid refugee claim because of the risk created by the Maras. This can not be.

[25] At best, the documentary evidence establishes that all Salvadorans face a generalized risk of violence from gangs. Pursuant to s. 97, the applicant had to establish that she faces a personalized risk to her life. If there is one category of persons which is at a higher risk of being targeted, it is the young men, who are the prime target of recruitment in El Salvador. But the evidence on the record is insufficient to demonstrate that young women are similarly at a significantly higher risk than the general population of being targeted by the street gangs. As a result, the Board made no error in failing to consider this issue specifically in its reasons.

[26] For all the foregoing reasons, this application for judicial review is dismissed. No questions for certification were proposed, and none is certified.


## 22604:2 · paragraphs 30-31

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `fe63fe1fb709560280e21e35dde1b5edbba684724d530305a6b9748c9a0fffc5`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22604:2:subtheme:1 · paragraphs 30-31

- Raw key terms: `application, batres, cause, citizenship, court, date, dismissed, docket`
- Display key terms: `batres, date, dismissed`
- Argument roles: `disposition`
- Explanation: Observed roles: disposition Display terms: batres, date, dismissed Operative outcome context: ORDER THIS COURT ORDERS that this application for judicial review is dismissed. Evidence spans paragraphs 30-31. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `disposition` cue `dismissed` at chunk `5060440` offsets `225-234`; context: ORDER
THIS COURT ORDERS that this application for judicial review is dismissed.

#### Section text

ORDER
THIS COURT ORDERS that this application for judicial review is dismissed.
"Yves de Montigny"
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET: IMM-2299-08
STYLE OF CAUSE: VENTURA SARAI BATRES VELASQUEZ v. MINISTER OF CITIZENSHIP AND IMMIGRATION
PLACE OF HEARING: Toronto, Ontario
DATE OF HEARING: October 28, 2008
REASONS FOR 

## 22604:3 · paragraphs 32-32

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `b25ec1d1ce197f0f8eff3d0a10a4a62d3ea9c0c78aa29a28da8276c23f428af8`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22604:3:subtheme:1 · paragraphs 32-32

- Raw key terms: `appearances, applicant, barrister, batres, citizenship, cohen, college, dated`
- Display key terms: `barrister, batres, cohen, college, dated`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: barrister, batres, cohen, college, dated No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 32-32. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

ORDER
AND ORDER: de Montigny, J.
DATED: February 2, 2009
APPEARANCES:
Mr. Neil Cohen
FOR THE APPLICANT
VENTURA SARAI BATRES VELASQUEZ
Mr. Manuel Mendelzon
FOR THE RESPONDENT
MINISTER OF CITIZENSHIP AND IMMIGRATION
SOLICITORS OF RECORD:
Mr. Neil Cohen
Barrister and Solicitor
2 College Street, Suite 115
Toronto, ON M5G 1K3
Fax: (416) 921-9542
FOR THE APPLICANT
VENTURA SARAI BATRES VELASQUEZ
Department of Justice
The Exchange Tower
130 King Street West
Suite 3400, Box 36
Toronto, ON M5X 1K6
Fax; (416) 354-8982
FOR THE RESPONDENT
MINISTER OF CITIZENSHIP AND IMMIGRATION
