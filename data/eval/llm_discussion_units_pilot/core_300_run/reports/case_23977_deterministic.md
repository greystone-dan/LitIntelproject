# Discussion Units: case 23977

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **14**
- Continuity pairs: **13**
- Discussion Units: **2**
- Paragraph source hashes: **14**
- Sub-themes: **4**

## 23977:1 · paragraphs 0-12

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `67226028b7a2a1644693952d97364f1a1b3afc7f64cdea773e3cfcd73a157c41`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 23977:1:subtheme:1 · paragraphs 0-7

- Raw key terms: `applicant, canada, decision, immigration, affidavit, agent, citizenship, reasons`
- Display key terms: `affidavit, agent`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, reasoning_application Display terms: affidavit, agent Rule/authority context: [1] The applicant applied for permanent residence in Canada under the Federal Skilled Worker (FSW) class on the basis of his stated experience under national occupational classification code (NOC) 7372, driller and blast | [3] A Citizenship and Immigration Canada agent determined that the applicant did not provide evidence that he satisfied this requirement and was not eligible for further processing pursuant to subsection 75(3) of the Reg Application context: [1] The applicant applied for permanent residence in Canada under the Federal Skilled Worker (FSW) class on the basis of his stated experience under national occupational classification code (NOC) 7372, driller and blast | The affidavit is therefore inadmissible. Evidence spans paragraphs 0-7. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `under` at chunk `5125628` offsets `60-65`; context: [1] The applicant applied for permanent residence in Canada under the Federal Skilled Worker (FSW) class on the basis of his stated experience under national occupational classification code (NOC) 7372, driller and blaster.
- Evidence: `reasoning_application` cue `applied` at chunk `5125628` offsets `18-25`; context: [1] The applicant applied for permanent residence in Canada under the Federal Skilled Worker (FSW) class on the basis of his stated experience under national occupational classification code (NOC) 7372, driller and blaster.
- Evidence: `evidence_fact` cue `determined that` at chunk `5125630` offsets `47-62`; context: [3] A Citizenship and Immigration Canada agent determined that the applicant did not provide evidence that he satisfied this requirement and was not eligible for further processing pursuant to subsection 75(3) of the Regulations.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5125630` offsets `181-192`; context: [3] A Citizenship and Immigration Canada agent determined that the applicant did not provide evidence that he satisfied this requirement and was not eligible for further processing pursuant to subsection 75(3) of the Regulations.
- Evidence: `evidence_fact` cue `affidavit` at chunk `5125631` offsets `242-251`; context: The agent subsequently swore an affidavit for this judicial review stating that the applicant’s evidence only demonstrated experience in two of the listed main duties.
- Evidence: `evidence_fact` cue `affidavit` at chunk `5125632` offsets `66-75`; context: [5] Decision makers may not supplement their reasons by way of an affidavit, but they may provide an explanation for their notes made contemporaneous to the decision: Taleb v Canada (Minister of Citizenship and Immigration), 2012 FC 384, paras 24-25.
- Evidence: `counterargument_limitation` cue `but` at chunk `5125632` offsets `77-80`; context: [5] Decision makers may not supplement their reasons by way of an affidavit, but they may provide an explanation for their notes made contemporaneous to the decision: Taleb v Canada (Minister of Citizenship and Immigration), 2012 FC 384, paras 24-25.
- Evidence: `evidence_fact` cue `affidavit` at chunk `5125633` offsets `99-108`; context: The affidavit was sworn on July 30, 2012, three months after the decision, casting doubt as to its reliability.
- Evidence: `reasoning_application` cue `therefore` at chunk `5125633` offsets `345-354`; context: The affidavit is therefore inadmissible.

#### 23977:1:subtheme:2 · paragraphs 8-10

- Raw key terms: `agent, court, decision, evidence, process, provides, reached, reasoning`
- Display key terms: `agent, process, provides, reached, reasoning`
- Argument roles: `counterargument_limitation, evidence_fact, issue`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue Display terms: agent, process, provides, reached, reasoning Evidence spans paragraphs 8-10. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5125635` offsets `348-355`; context: It is not for this Court to determine whether the applicant has in fact performed the actions described in the lead statement and a substantial number of the main duties.
- Evidence: `evidence_fact` cue `evidence` at chunk `5125635` offsets `254-262`; context: ” There are six main duties listed, several of which could arguably correspond with the tasks described in the applicant’s evidence, particularly (b) (e) (g) and (h) noted above.
- Evidence: `evidence_fact` cue `evidence` at chunk `5125637` offsets `392-400`; context: Where readily apparent, evidentiary lacunae may be filled in when supported by the evidence, and logical inferences, implicit to the result but not expressly drawn.
- Evidence: `counterargument_limitation` cue `but` at chunk `5125637` offsets `449-452`; context: Where readily apparent, evidentiary lacunae may be filled in when supported by the evidence, and logical inferences, implicit to the result but not expressly drawn.

#### 23977:1:subtheme:3 · paragraphs 11-12

- Raw key terms: `citizenship, immigration, reasons, agent, agent's, allows, application, april`
- Display key terms: `agent, agent's, allows, april`
- Argument roles: `disposition, governing_rule, issue`
- Explanation: Observed roles: disposition, governing_rule, issue Display terms: agent, agent's, allows, april Rule/authority context: It is ironic that Newfoundland Nurses, a case which at its core is about deference and standard of review, is urged as authority for the supervisory court to do the task that the decision maker did not do, to supply the  Operative outcome context: JUDGMENT THIS COURT’S JUDGMENT is that the application for judicial review is granted. Evidence spans paragraphs 11-12. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5125638` offsets `299-304`; context: This is particularly so where the reasons are silent on a critical issue.
- Evidence: `governing_rule` cue `standard of review` at chunk `5125638` offsets `393-411`; context: It is ironic that Newfoundland Nurses, a case which at its core is about deference and standard of review, is urged as authority for the supervisory court to do the task that the decision maker did not do, to supply the reasons that might have been given and make findings of fact that were not made.
- Evidence: `disposition` cue `granted` at chunk `5125638` offsets `920-927`; context: JUDGMENT
THIS COURT’S JUDGMENT is that the application for judicial review is granted.

#### Section text

Komolafe v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2013-04-25
Neutral citation
2013 FC 431
File numbers
IMM-4639-12
Decision Content
Federal Court
Cour fédérale
Date: 20130425
Docket: IMM-4639-12
Citation: 2013 FC 431
Ottawa, Ontario, April 25, 2013
PRESENT: The Honourable Mr. Justice Rennie
BETWEEN:
OLUDARE AYODELE KOMOLAFE
Applicant
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
REASONS FOR JUDGMENT AND JUDGMENT

[1] The applicant applied for permanent residence in Canada under the Federal Skilled Worker (FSW) class on the basis of his stated experience under national occupational classification code (NOC) 7372, driller and blaster. He has a bachelor’s degree in geology and a certificate in blasting from the Ministry of Mines and Steel Development in Nigeria. He is employed as a quarry supervisor in Nigeria.

[2] Subsection 75(2) of the Immigration and Refugee Protection Regulations, SOR/2002-227 (Regulations) describes a skilled worker as, inter alia, a foreign national who has performed the tasks described in the lead statement for the occupation as set out in the NOC occupational descriptions and performed a substantial number of the main duties of the occupation, including all “essential” duties.

[3] A Citizenship and Immigration Canada agent determined that the applicant did not provide evidence that he satisfied this requirement and was not eligible for further processing pursuant to subsection 75(3) of the Regulations.

[4] The decision is a form letter which states that the agent was not satisfied that the applicant had performed the actions in the lead statement for the occupation or a substantial number of the main duties. The agent subsequently swore an affidavit for this judicial review stating that the applicant’s evidence only demonstrated experience in two of the listed main duties.

[5] Decision makers may not supplement their reasons by way of an affidavit, but they may provide an explanation for their notes made contemporaneous to the decision: Taleb v Canada (Minister of Citizenship and Immigration), 2012 FC 384, paras 24-25.

[6] In this case, the agent has no contemporaneous notes which describe her reasoning process. The affidavit was sworn on July 30, 2012, three months after the decision, casting doubt as to its reliability. It necessarily goes beyond explaining the agent’s notes, as there are none, and is tendered as reasons for the decision. The affidavit is therefore inadmissible.

[7] The applicant’s employer provided a letter stating that, among other things, he: (a) schedules, supervises and coordinates drilling operations, (b) maps the pattern of holes and determines their size and spacing, (c) decides when to suspend or continue drilling, (d) calculates the amount of explosives required, (e) supervises subordinates in carrying out charging operations, (g) ensures safety precautions are followed, and (h) connects the blasting circuit.

[8] The NOC occupational description states that, “Blasters in this group fill blast holes with explosives and detonate explosives.” There are six main duties listed, several of which could arguably correspond with the tasks described in the applicant’s evidence, particularly (b) (e) (g) and (h) noted above. It is not for this Court to determine whether the applicant has in fact performed the actions described in the lead statement and a substantial number of the main duties. The agent must do so, with some line of reasoning which provides a basis for review. As Justice Richard Mosley found in Gulati v Canada (Citizenship and Immigration), 2010 FC 451, it is impossible to assess the reasonableness of the officer’s conclusions without knowing which duties had not been performed.

[9] The decision provides no insight into the agent’s reasoning process. The agent merely stated her conclusion, without explanation. It is entirely unclear why the decision was reached.

[10] Newfoundland and Labrador Nurses' Union v Newfoundland and Labrador (Treasury Board), 2011 SCC 62, [2011] 3 SCR 708 does not save the decision. Newfoundland Nurses ensures that the focus of judicial review remains on the outcome or decision itself, and not the process by which that outcome was reached. Where readily apparent, evidentiary lacunae may be filled in when supported by the evidence, and logical inferences, implicit to the result but not expressly drawn. A reviewing court looks to the record with a view to upholding the decision.

[11] Newfoundland Nurses is not an open invitation to the Court to provide reasons that were not given, nor is it licence to guess what findings might have been made or to speculate as to what the tribunal might have been thinking. This is particularly so where the reasons are silent on a critical issue. It is ironic that Newfoundland Nurses, a case which at its core is about deference and standard of review, is urged as authority for the supervisory court to do the task that the decision maker did not do, to supply the reasons that might have been given and make findings of fact that were not made. This is to turn the jurisprudence on its head. Newfoundland Nurses allows reviewing courts to connect the dots on the page where the lines, and the direction they are headed, may be readily drawn. Here, there were no dots on the page.
JUDGMENT
THIS COURT’S JUDGMENT is that the application for judicial review is granted. The agent's decision is set aside, and the matter is referred back to Citizenship and Immigration Canada for reconsideration by a different agent. There is no question for certification.
"Donald J. Rennie"
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET: IMM-4639-12
STYLE OF CAUSE: OLUDARE AYODELE KOMOLAFE v THE MINISTER OF CITIZENSHIP AND IMMIGRATION
PLACE OF HEARING: Toronto, Ontario
DATE OF HEARING: April 10, 2013
REASONS FOR 

## 23977:2 · paragraphs 13-13

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `4f2ee73fe8d8023f3bb074e62763313ce10ba933debc9fcd162f522a1f8b0752`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 23977:2:subtheme:1 · paragraphs 13-13

- Raw key terms: `appearances, applicant, april, attorney, canada, casimir, clark, dated`
- Display key terms: `april, casimir, clark, dated`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: april, casimir, clark, dated No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 13-13. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT
AND JUDGMENT: RENNIE J.
DATED: April 25, 2013
APPEARANCES:
Mr. Casimir Eziefule
FOR THE APPLICANT
Ms. Jocelyn Espejo Clark
FOR THE RESPONDENT
SOLICITORS OF RECORD:
Casimir Eziefule
Windsor, Ontario
FOR THE APPLICANT
William F. Pentney,
Deputy Attorney General of Canada
Toronto, Ontario
FOR THE RESPONDENT
