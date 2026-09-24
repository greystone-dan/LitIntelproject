# Discussion Units: case 22752

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **40**
- Continuity pairs: **39**
- Discussion Units: **2**
- Paragraph source hashes: **40**
- Sub-themes: **9**

## 22752:1 · paragraphs 0-38

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `49a43dfbf4babf2cb2c8c0f2327c9c119abacfa60d05a100e36b4915de1463cd`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22752:1:subtheme:1 · paragraphs 0-2

- Raw key terms: `applicant, alejandro, decision, immigration, action, alleges, application, background`
- Display key terms: `alejandro, action, alleges, background`
- Argument roles: `governing_rule, party_position, reasoning_application`
- Explanation: Observed roles: governing_rule, party_position, reasoning_application Display terms: alejandro, action, alleges, background Position/evidence statements: He claims to fear persecution in his country of origin because his fellow journalists are not safe there and are being killed. Rule/authority context: [1] This is an application for judicial review under subsection 72(1) of the Immigration and Refugee Protection Act, S. Application context: He alleges that he was verbally and physically threatened by members of two political parties in Mexico, the Institutional Revolutionary Party (PRI) and the National Action Party (PAN), because of his career as a journal Evidence spans paragraphs 0-2. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `under` at chunk `5066605` offsets `47-52`; context: [1] This is an application for judicial review under subsection 72(1) of the Immigration and Refugee Protection Act, S.
- Evidence: `party_position` cue `claims` at chunk `5066606` offsets `415-421`; context: He claims to fear persecution in his country of origin because his fellow journalists are not safe there and are being killed.
- Evidence: `reasoning_application` cue `because` at chunk `5066606` offsets `287-294`; context: He alleges that he was verbally and physically threatened by members of two political parties in Mexico, the Institutional Revolutionary Party (PRI) and the National Action Party (PAN), because of his career as a journalist on Mexican television and radio and the political opinions imputed to him as a result.

#### 22752:1:subtheme:2 · paragraphs 3-6

- Raw key terms: `applicant, according, claim, country, leave, mexican, political, politicians`
- Display key terms: `according, country, leave, mexican, political, politicians`
- Argument roles: `evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, reasoning_application Display terms: according, country, leave, mexican, political, politicians Application context: He ruled out any internal flight alternative in Mexico because the political parties were present throughout the country. Evidence spans paragraphs 3-6. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5066607` offsets `244-250`; context: [3] According to the applicant’s personal information form (PIF), he held several positions in Mexican broadcasting, including news reader, entertainment program host and, more recently, host of a phone‑in program dealing mainly with political issues.
- Evidence: `reasoning_application` cue `because` at chunk `5066609` offsets `140-147`; context: He ruled out any internal flight alternative in Mexico because the political parties were present throughout the country.
- Evidence: `evidence_fact` cue `found that` at chunk `5066610` offsets `52-62`; context: [6] The panel accepted the applicant’s identity but found that his narrative was contradictory and implausible.

#### 22752:1:subtheme:3 · paragraphs 7-8

- Raw key terms: `applicant, concerning, employment, filed, hidalgo, panel, abuses, according`
- Display key terms: `concerning, employment, filed, hidalgo, abuses, according`
- Argument roles: `disposition, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, issue, party_position, reasoning_application Display terms: concerning, employment, filed, hidalgo, abuses, according Position/evidence statements: He could not spontaneously name the governor of the state of Hidalgo but remembered the name of the governor’s wife, despite the fact that he claimed to be an investigative journalist who was up to date on political abus Application context: The panel pointed out that, even if he was unable to obtain a cessation of employment letter, he could have tried to obtain a letter describing his run‑ins with the police, which allegedly resulted in him leaving his job Operative outcome context: The complaint filed by the applicant with the preliminary investigation branch following the 2004 incident did not name a Nissan representative, and the applicant was unable to establish what kind of protection he was al Evidence spans paragraphs 7-8. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5066611` offsets `570-577`; context: When asked whether the PRI and the PAN routinely killed journalists in Mexico, he stated that this was the case and added that that they even killed each other.
- Evidence: `party_position` cue `claimed` at chunk `5066611` offsets `240-247`; context: He could not spontaneously name the governor of the state of Hidalgo but remembered the name of the governor’s wife, despite the fact that he claimed to be an investigative journalist who was up to date on political abuses;
b.
- Evidence: `evidence_fact` cue `testimony` at chunk `5066611` offsets `84-93`; context: [7] The panel drew adverse inferences concerning several aspects of the applicant’s testimony:
a.
- Evidence: `reasoning_application` cue `because` at chunk `5066611` offsets `1459-1466`; context: The panel pointed out that, even if he was unable to obtain a cessation of employment letter, he could have tried to obtain a letter describing his run‑ins with the police, which allegedly resulted in him leaving his job because of the risk he believed he was facing;
g.
- Evidence: `disposition` cue `denied` at chunk `5066611` offsets `1737-1743`; context: The complaint filed by the applicant with the preliminary investigation branch following the 2004 incident did not name a Nissan representative, and the applicant was unable to establish what kind of protection he was allegedly denied;
h.

#### 22752:1:subtheme:4 · paragraphs 9-16

- Raw key terms: `panel, applicant, evidence, knowledge, protection, specialized, because, mexico`
- Display key terms: `knowledge, protection, specialized, because, mexico`
- Argument roles: `evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, party_position, reasoning_application Display terms: knowledge, protection, specialized, because, mexico Position/evidence statements: The applicant stated that he was aware of this possibility of complaining but argued that, in reality, it did not work unless one could back up one’s statement. | The applicant argues that the panel erred in refusing to analyse that documentary evidence, which confirmed that he was in fact a journalist in Mexico. Application context: The applicant alleged that, when he went to complain, he was told that there was no point in filing a complaint because he was not injured. | According to the applicant, the DVD was evidence that was material to his claim because it showed the work he did as a journalist, which was the basis for his fear of persecution. Evidence spans paragraphs 9-16. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Issues` at chunk `5066613` offsets `1022-1028`; context: Issues
- Evidence: `party_position` cue `argued` at chunk `5066613` offsets `939-945`; context: The applicant stated that he was aware of this possibility of complaining but argued that, in reality, it did not work unless one could back up one’s statement.
- Evidence: `reasoning_application` cue `because` at chunk `5066613` offsets `239-246`; context: The applicant alleged that, when he went to complain, he was told that there was no point in filing a complaint because he was not injured.
- Evidence: `issue` cue `issues` at chunk `5066614` offsets `53-59`; context: [10] This application for judicial review raises two issues, which can be summarized as follows:
1.
- Evidence: `evidence_fact` cue `evidence` at chunk `5066614` offsets `135-143`; context: Did the panel err in assessing the evidence?
- Evidence: `evidence_fact` cue `evidence` at chunk `5066615` offsets `194-202`; context: According to the applicant, the DVD was evidence that was material to his claim because it showed the work he did as a journalist, which was the basis for his fear of persecution.
- Evidence: `reasoning_application` cue `because` at chunk `5066615` offsets `234-241`; context: According to the applicant, the DVD was evidence that was material to his claim because it showed the work he did as a journalist, which was the basis for his fear of persecution.
- Evidence: `party_position` cue `argues` at chunk `5066616` offsets `180-186`; context: The applicant argues that the panel erred in refusing to analyse that documentary evidence, which confirmed that he was in fact a journalist in Mexico.
- Evidence: `evidence_fact` cue `evidence` at chunk `5066616` offsets `248-256`; context: The applicant argues that the panel erred in refusing to analyse that documentary evidence, which confirmed that he was in fact a journalist in Mexico.
- Evidence: `reasoning_application` cue `because` at chunk `5066616` offsets `130-137`; context: [12] In its reasons, the panel referred to those two documents but stated that it could not attach any probative value to the DVD because it had not been translated.
- Evidence: `party_position` cue `argues` at chunk `5066617` offsets `20-26`; context: [13] The respondent argues that the panel was well‑founded in law not to consider the DVD, which had not been translated into one of the official languages as required by Rule 28 of the Refugee Protection Division Rules, SOR/2002‑228 (Rules), which reads as follows:
28.
- Evidence: `party_position` cue `submits` at chunk `5066618` offsets `259-266`; context: The respondent submits that no documentary evidence could influence the negative findings of fact already made by the panel with regard to the applicant’s credibility.
- Evidence: `evidence_fact` cue `testimony` at chunk `5066618` offsets `233-242`; context: [14] The respondent maintains that, even if the panel had accepted the fact that the applicant was a journalist in Mexico, the negative decision was based on the cumulative implausibilities and discrepancies in his narrative and his testimony.
- Evidence: `party_position` cue `argues` at chunk `5066620` offsets `19-25`; context: [16] The applicant argues that the panel’s “specialized knowledge” had to be based on independent documentary evidence and that he had to be given that evidence so he could respond to it.
- Evidence: `evidence_fact` cue `evidence` at chunk `5066620` offsets `110-118`; context: [16] The applicant argues that the panel’s “specialized knowledge” had to be based on independent documentary evidence and that he had to be given that evidence so he could respond to it.
- Evidence: `reasoning_application` cue `because` at chunk `5066620` offsets `267-274`; context: The applicant alleges that the panel erred in its analysis of state protection because it relied in large part on evidence that had not been filed.

#### 22752:1:subtheme:5 · paragraphs 17-18

- Raw key terms: `applicant, credibility, knowledge, panel, specialized, allegations, analyse, analysis`
- Display key terms: `credibility, knowledge, specialized, allegations, analyse, analysis`
- Argument roles: `evidence_fact, issue, party_position`
- Explanation: Observed roles: evidence_fact, issue, party_position Display terms: credibility, knowledge, specialized, allegations, analyse, analysis Position/evidence statements: [17] The respondent submits that the panel’s decision was based on the applicant’s lack of credibility and not on the question of state protection. Evidence spans paragraphs 17-18. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5066621` offsets `118-126`; context: [17] The respondent submits that the panel’s decision was based on the applicant’s lack of credibility and not on the question of state protection.
- Evidence: `party_position` cue `submits` at chunk `5066621` offsets `20-27`; context: [17] The respondent submits that the panel’s decision was based on the applicant’s lack of credibility and not on the question of state protection.
- Evidence: `evidence_fact` cue `evidence` at chunk `5066622` offsets `228-236`; context: First, the panel erred in refusing to analyse evidence that was material to his claim.

#### 22752:1:subtheme:6 · paragraphs 19-31

- Raw key terms: `panel, applicant, evidence, paragraph, canada, immigration, credibility, citizenship`
- Display key terms: `paragraph, credibility`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position, reasoning_application Display terms: paragraph, credibility Position/evidence statements: [19] The applicant submits that reasonableness is the only test that must be used on judicial review. | [24] Contrary to what the applicant argues, the language used in the panel’s written reasons indicates that the decision maker took due account of the DVD in its analysis. Application context: New Brunswick, 2008 SCC 9, applies. | [22] In this case, the panel concluded that the applicant lacked credibility and therefore rejected his claim for refugee protection. Evidence spans paragraphs 19-31. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5066623` offsets `135-141`; context: According to the respondent, the issues in this case relate to the interpretation of evidence and the questions of fact identified by the panel.
- Evidence: `party_position` cue `submits` at chunk `5066623` offsets `19-26`; context: [19] The applicant submits that reasonableness is the only test that must be used on judicial review.
- Evidence: `evidence_fact` cue `evidence` at chunk `5066623` offsets `187-195`; context: According to the respondent, the issues in this case relate to the interpretation of evidence and the questions of fact identified by the panel.
- Evidence: `issue` cue `whether` at chunk `5066624` offsets `344-351`; context: My task is to ascertain whether the impugned decision is reasonably justified in light of the evidence and the state of the relevant law: Luis c.
- Evidence: `evidence_fact` cue `evidence` at chunk `5066624` offsets `414-422`; context: My task is to ascertain whether the impugned decision is reasonably justified in light of the evidence and the state of the relevant law: Luis c.
- Evidence: `reasoning_application` cue `applies` at chunk `5066624` offsets `199-206`; context: New Brunswick, 2008 SCC 9, applies.
- Evidence: `evidence_fact` cue `evidence` at chunk `5066625` offsets `636-644`; context: A subjective fear of persecution is solely based on the assessment of the applicant’s credibility while the objective fear is usually established by documentary evidence regarding the country conditions.
- Evidence: `evidence_fact` cue `evidence` at chunk `5066626` offsets `221-229`; context: The applicant criticizes the panel for not considering, in its analysis, corroborating evidence that supported his testimony, including the DVD concerning his employment.
- Evidence: `reasoning_application` cue `therefore` at chunk `5066626` offsets `81-90`; context: [22] In this case, the panel concluded that the applicant lacked credibility and therefore rejected his claim for refugee protection.
- Evidence: `party_position` cue `argues` at chunk `5066628` offsets `36-42`; context: [24] Contrary to what the applicant argues, the language used in the panel’s written reasons indicates that the decision maker took due account of the DVD in its analysis.
- Evidence: `counterargument_limitation` cue `However` at chunk `5066628` offsets `319-326`; context: However, the panel did not give the DVD any weight, and for good reason, since it had not been translated.
- Evidence: `party_position` cue `argues` at chunk `5066629` offsets `19-25`; context: [25] The applicant argues, and correctly so, that administrative tribunals are generally not bound by the strict rules of evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `5066629` offsets `122-130`; context: [25] The applicant argues, and correctly so, that administrative tribunals are generally not bound by the strict rules of evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `5066630` offsets `52-60`; context: [26] The applicant was entitled to file documentary evidence to support his subjective fear.
- Evidence: `reasoning_application` cue `therefore` at chunk `5066630` offsets `815-824`; context: The panel was therefore entitled to attach no probative value to it.
- Evidence: `counterargument_limitation` cue `However` at chunk `5066630` offsets `93-100`; context: However, as the respondent notes, Rule 28 provides that “[a]ll documents used at a proceeding must be in English or French or, if in another language, be provided with an English or French translation and a translator’s declaration”.
- Evidence: `evidence_fact` cue `testimony` at chunk `5066631` offsets `239-248`; context: In particular, the panel found omissions, contradictions between his PIF and his testimony at the hearing and implausibilities in his narrative.
- Evidence: `party_position` cue `submitted` at chunk `5066632` offsets `406-415`; context: The panel is in the best position to assess the explanations submitted by claimants for any perceived inconsistencies and implausibilities.
- Evidence: `evidence_fact` cue `evidence` at chunk `5066632` offsets `109-117`; context: [28] It is already well established that the Board’s decisions on questions of credibility and assessment of evidence are entitled to great deference by the Court: Zavala v.
- Evidence: `evidence_fact` cue `testimony` at chunk `5066633` offsets `154-163`; context: [29] In my opinion, the panel’s finding on the applicant’s credibility is not unreasonable in light of the many discrepancies and implausibilities in his testimony.
- Evidence: `evidence_fact` cue `evidence` at chunk `5066634` offsets `436-444`; context: 238, the Federal Court of Appeal held that a tribunal’s perception that the applicant is not credible on an important aspect of the claim can amount to a finding that there is no credible evidence on which the claim can be based.
- Evidence: `reasoning_application` cue `I find` at chunk `5066634` offsets `161-167`; context: Canada (Minister of Citizenship and Immigration), 2004 FC 636, an extract that I find interesting for our purposes:
.
- Evidence: `reasoning_application` cue `concludes` at chunk `5066635` offsets `19-28`; context: [31] Where a panel concludes that a claimant is not credible, it is not obliged to explain everything that supports the allegations that are contrary to the allegations it accepts.

#### 22752:1:subtheme:7 · paragraphs 32-36

- Raw key terms: `knowledge, specialized, applicant, evidence, panel, rule, claimant, decision`
- Display key terms: `knowledge, specialized, rule`
- Argument roles: `evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, party_position, reasoning_application Display terms: knowledge, specialized, rule Position/evidence statements: [33] The applicant argues that the panel’s “specialized knowledge” had to be based on documentary evidence and that he had to be given that evidence at the time of the hearing so he could respond to it. | 1515, unverifiable personal knowledge does not qualify as specialized knowledge: The applicant submits (and I agree), that the personal and/or professional experiences of the Board members, the full extent of which was u Application context: Therefore, in order for Rule 18 to be effective, the RPD member who declares specialized knowledge must place on the record sufficient detail of the knowledge so as to allow it to be tested. | The “knowledge” relied on in this case was neither quantifiable nor verifiable, which meant that Rule 18 did not apply. Evidence spans paragraphs 32-36. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5066636` offsets `16-21`; context: [32] The second issue concerns the panel’s “specialized knowledge”.
- Evidence: `evidence_fact` cue `record` at chunk `5066636` offsets `84-90`; context: A review of the record shows that the panel drew on its specialized knowledge to explain to the applicant that there are refugee protection claimants who have filed complaints with the Mexican authorities without necessarily being injured or on their deathbed.
- Evidence: `party_position` cue `argues` at chunk `5066637` offsets `19-25`; context: [33] The applicant argues that the panel’s “specialized knowledge” had to be based on documentary evidence and that he had to be given that evidence at the time of the hearing so he could respond to it.
- Evidence: `evidence_fact` cue `evidence` at chunk `5066637` offsets `98-106`; context: [33] The applicant argues that the panel’s “specialized knowledge” had to be based on documentary evidence and that he had to be given that evidence at the time of the hearing so he could respond to it.
- Evidence: `evidence_fact` cue `evidence` at chunk `5066638` offsets `459-467`; context: Before using any information or opinion that is within its specialized knowledge, the Division must notify the claimant or protected person, and the Minister if the Minister is present at the hearing, and give them a chance to
(a) make representations on the reliability and use of the information or opinion; and
(b) give evidence in support of their representations.
- Evidence: `party_position` cue `submits` at chunk `5066639` offsets `800-807`; context: 1515, unverifiable personal knowledge does not qualify as specialized knowledge:
The applicant submits (and I agree), that the personal and/or professional experiences of the Board members, the full extent of which was unclear, hardly justified their claim to “specialized knowledge”.
- Evidence: `evidence_fact` cue `record` at chunk `5066639` offsets `461-467`; context: Therefore, in order for Rule 18 to be effective, the RPD member who declares specialized knowledge must place on the record sufficient detail of the knowledge so as to allow it to be tested.
- Evidence: `reasoning_application` cue `Therefore` at chunk `5066639` offsets `344-353`; context: Therefore, in order for Rule 18 to be effective, the RPD member who declares specialized knowledge must place on the record sufficient detail of the knowledge so as to allow it to be tested.
- Evidence: `reasoning_application` cue `apply` at chunk `5066640` offsets `496-501`; context: The “knowledge” relied on in this case was neither quantifiable nor verifiable, which meant that Rule 18 did not apply.

#### 22752:1:subtheme:8 · paragraphs 37-38

- Raw key terms: `adjudges, alejandro, applicant, application, brian, case, cause, certified`
- Display key terms: `adjudges, alejandro, brian, case, certified`
- Argument roles: `disposition, issue`
- Explanation: Observed roles: disposition, issue Display terms: adjudges, alejandro, brian, case, certified Operative outcome context: JUDGMENT THIS COURT ORDERS AND ADJUDGES that the application for judicial review be dismissed. Evidence spans paragraphs 37-38. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5066641` offsets `538-546`; context: There is no question of general importance to be certified.
- Evidence: `disposition` cue `dismissed` at chunk `5066641` offsets `515-524`; context: JUDGMENT
THIS COURT ORDERS AND ADJUDGES that the application for judicial review be dismissed.

#### Section text

Hernandez Cortes v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2009-06-04
Neutral citation
2009 FC 583
File numbers
IMM-4645-08
Decision Content
Federal Court
Cour fédérale
Date: 20090604
Docket: IMM-4645-08
Citation: 2009 FC 583
Ottawa, Ontario, June 4, 2009
PRESENT: The Honourable Max M. Teitelbaum
BETWEEN:
JOSUE ALEJANDRO HERNANDEZ CORTES
Applicant
and
THE MINISTER OF CITIZENSHIP
AND IMMIGRATION
Respondent
REASONS FOR JUDGMENT AND JUDGMENT

[1] This is an application for judicial review under subsection 72(1) of the Immigration and Refugee Protection Act, S.C. 2001, c. 27 (IRPA), of a decision made on September 18, 2008 by the Refugee Protection Division of the Immigration and Refugee Board (the panel or the Board) finding that the applicant is not a Convention refugee or a person in need of protection within the meaning of sections 96 and 97 of the IRPA.
Factual background

[2] The applicant, Josuè Alejandro Hernàndez Cortès, is a Mexican citizen from the state of Hidalgo. He alleges that he was verbally and physically threatened by members of two political parties in Mexico, the Institutional Revolutionary Party (PRI) and the National Action Party (PAN), because of his career as a journalist on Mexican television and radio and the political opinions imputed to him as a result. He claims to fear persecution in his country of origin because his fellow journalists are not safe there and are being killed.

[3] According to the applicant’s personal information form (PIF), he held several positions in Mexican broadcasting, including news reader, entertainment program host and, more recently, host of a phone‑in program dealing mainly with political issues. In the last of these positions, he took calls from the public and interviewed politicians, and he had to do his own research to ensure that his opinions were informed and neutral.

[4] Three events allegedly led him to flee the country. In 2004, he criticized the quality of a Nissan car during one of his shows, and this led to a Nissan representative—who also happened to be a politician—threatening to destroy his career as a television journalist. He says that in 2005, he was attacked by someone driving a Nissan car. In 2006, the applicant was summoned to a restaurant, where he was told that he would be killed if he continued to talk about politicians the way he did and he was given two months to leave the city. According to the applicant, the complaints he filed with the Mexican authorities led nowhere.

[5] The applicant decided to leave Mexico in December 2006 to seek refuge in Canada. He ruled out any internal flight alternative in Mexico because the political parties were present throughout the country. The Board heard his claim for refugee protection on May 14, 2008 and made a negative decision on September 18, 2008.
Impugned decision

[6] The panel accepted the applicant’s identity but found that his narrative was contradictory and implausible. After analysing all the evidence, the panel concluded that his claim for refugee protection was not credible.

[7] The panel drew adverse inferences concerning several aspects of the applicant’s testimony:
a. He could not spontaneously name the governor of the state of Hidalgo but remembered the name of the governor’s wife, despite the fact that he claimed to be an investigative journalist who was up to date on political abuses;
b. When asked who had won the last presidential election in the state of Hidalgo and with how many seats, he answered that the PRI had won, but he did not know with how many seats. He later testified that the PAN had been victorious;
c. When asked whether the PRI and the PAN routinely killed journalists in Mexico, he stated that this was the case and added that that they even killed each other. The panel noted that he had previously testified that these two political parties were so similar that they were interchangeable;
d. The applicant had no information about the publicized murder of Lus Amaldo Portosio in 2000, which had been ordered by President Zedillo’s brother;
e. The applicant did not know the names of his fellow journalists killed by drug traffickers and was unable to provide documentary evidence about this;
f. The applicant testified that he had stopped working without informing his bosses. The panel pointed out that, even if he was unable to obtain a cessation of employment letter, he could have tried to obtain a letter describing his run‑ins with the police, which allegedly resulted in him leaving his job because of the risk he believed he was facing;
g. The complaint filed by the applicant with the preliminary investigation branch following the 2004 incident did not name a Nissan representative, and the applicant was unable to establish what kind of protection he was allegedly denied;
h. The applicant failed to mention in his PIF that his brother had called the police at the time of the 2005 incident and that the police had quickly begun pursuing the Nissan car but had been unable to take down the licence plate number. The panel noted that this “omission” was evidence that the state had taken some measures to deal with this hit‑and‑run offence;
i. According to the applicant’s testimony at the hearing, he complained four times, but his PIF refers to only two complaints.

[8] The only proof of employment filed by the applicant was a card stating that he was a radio host at the 89.3 FM radio station in the Hidalgo broadcasting system and a DVD concerning his work. Since the DVD had not been translated, the panel decided that it could not attach any probative value to it.

[9] The panel did not believe the applicant’s statement that he had tried to obtain protection from the authorities in Mexico. The applicant alleged that, when he went to complain, he was told that there was no point in filing a complaint because he was not injured. The panel drew on its specialized knowledge of Mexican cases to point out to the claimant that this was the first time it had heard such an argument and that refugee protection claimants do file complaints with the Mexican authorities without necessarily being injured or on their deathbed. The panel also referred to a document available on the Internet entitled Procedures followed to file a complaint with the Federal Prosecutor’s Office, which described three ways to file a complaint with the internal comptroller concerning irregularities committed by the Federal Prosecutor’s personnel. The applicant stated that he was aware of this possibility of complaining but argued that, in reality, it did not work unless one could back up one’s statement.
Issues

[10] This application for judicial review raises two issues, which can be summarized as follows:
1. Did the panel err in assessing the evidence?
2. Did the panel err in drawing on its specialized knowledge?
Positions of the parties
Assessment of the evidence

[11] The applicant filed documents to support his fear of persecution in Mexico, including a press card and a DVD concerning his professional activities. According to the applicant, the DVD was evidence that was material to his claim because it showed the work he did as a journalist, which was the basis for his fear of persecution.

[12] In its reasons, the panel referred to those two documents but stated that it could not attach any probative value to the DVD because it had not been translated. The applicant argues that the panel erred in refusing to analyse that documentary evidence, which confirmed that he was in fact a journalist in Mexico. He submits that the Refugee Protection Division is an administrative tribunal that is not bound by the strict rules of evidence and has a power to investigate. He further submits that the panel had the resources needed to examine the DVD, especially since a Spanish‑French interpreter was present at the hearing.

[13] The respondent argues that the panel was well‑founded in law not to consider the DVD, which had not been translated into one of the official languages as required by Rule 28 of the Refugee Protection Division Rules, SOR/2002‑228 (Rules), which reads as follows:
28.(1) All documents used at a proceeding must be in English or French or, if in another language, be provided with an English or French translation and a translator’s declaration.
28.(1) Tout document utilisé dans une procédure doit être rédigé en français ou en anglais ou, s’il est rédigé dans une autre langue, être accompagné d’une traduction française ou anglaise et de la déclaration du traducteur.

[14] The respondent maintains that, even if the panel had accepted the fact that the applicant was a journalist in Mexico, the negative decision was based on the cumulative implausibilities and discrepancies in his narrative and his testimony. The respondent submits that no documentary evidence could influence the negative findings of fact already made by the panel with regard to the applicant’s credibility.
Specialized knowledge

[15] The second ground for the application for judicial review is that the panel relied on its “specialized knowledge” to point out to the applicant that this was the first time it had heard such an argument and that refugee protection claimants do file complaints with the Mexican authorities without necessarily being injured or on their deathbed.

[16] The applicant argues that the panel’s “specialized knowledge” had to be based on independent documentary evidence and that he had to be given that evidence so he could respond to it. The applicant alleges that the panel erred in its analysis of state protection because it relied in large part on evidence that had not been filed.

[17] The respondent submits that the panel’s decision was based on the applicant’s lack of credibility and not on the question of state protection. In any event, the respondent argues that the panel was entitled to rely on its specialized knowledge of the availability of state protection in Mexico to question the applicant’s allegations.
Analysis
Standard of judicial review

[18] The applicant does not seem to be challenging the panel’s findings of fact with regard to his credibility. In his written representations, he makes the following two arguments. First, the panel erred in refusing to analyse evidence that was material to his claim. Second, the panel erred in drawing on its specialized knowledge without any corroboration or documentary evidence to back it up.

[19] The applicant submits that reasonableness is the only test that must be used on judicial review. According to the respondent, the issues in this case relate to the interpretation of evidence and the questions of fact identified by the panel. In his view, these questions must be assessed in the context of the standard set out in paragraph 18.1(4)(d) of the Federal Courts Act, SOR/98‑106.

[20] In my opinion, these proceedings raise questions of mixed law and fact, which means that the standard of reasonableness as defined by the Supreme Court in Dunsmuir v. New Brunswick, 2008 SCC 9, applies. The decision of the panel, which has some expertise in cases like this one, is therefore entitled to deference. My task is to ascertain whether the impugned decision is reasonably justified in light of the evidence and the state of the relevant law: Luis c. Canada (Ministre de la Citoyenneté et de l’Immigration), 2009 CF 352, at paragraph 9.
Assessment of the evidence

[21] It is well established that the burden of proof is on the applicant. In Hafeez v. Canada (Minister of Citizenship and Immigration), 2004 FC 1489, Mr. Justice Beaudry referred to this principle at paragraph 10:
. . . In order to succeed, the applicant needs to prove, on a balance of probabilities, that he has a reasonable subjective fear of persecution and that this subjective fear is objectively well‑founded (Canada (Attorney General) v. Ward, [1993] 2 S.C.R. 689). A subjective fear of persecution is solely based on the assessment of the applicant’s credibility while the objective fear is usually established by documentary evidence regarding the country conditions.

[22] In this case, the panel concluded that the applicant lacked credibility and therefore rejected his claim for refugee protection. The applicant criticizes the panel for not considering, in its analysis, corroborating evidence that supported his testimony, including the DVD concerning his employment.

[23] In its written reasons, the panel stated the following about the proof of employment:
The only proof of employment filed by the claimant is a card stating that the claimant is a radio host at the 89.3 FM radio station in the Hidalgo broadcasting system and a compact disc that appears to be a collection of the claimant’s television pursuits. Since this document has not been translated, the panel cannot attach any probative value to it.

[24] Contrary to what the applicant argues, the language used in the panel’s written reasons indicates that the decision maker took due account of the DVD in its analysis. In fact, the panel considered the DVD by noting in its written reasons that it appeared to be a collection of the applicant’s television pursuits. However, the panel did not give the DVD any weight, and for good reason, since it had not been translated.

[25] The applicant argues, and correctly so, that administrative tribunals are generally not bound by the strict rules of evidence. Moreover, paragraph 170(g) of the IRPA provides that the Refugee Protection Division is not bound by any legal or technical rules of evidence. In N.O. v. Canada (Minister of Citizenship and Immigration), 2004 FC 1552, Mr. Justice Harrington noted that the rules of evidence are made flexible specifically to allow refugee status claimants to present evidence that would ordinarily not be admissible (at paragraph 15).

[26] The applicant was entitled to file documentary evidence to support his subjective fear. However, as the respondent notes, Rule 28 provides that “[a]ll documents used at a proceeding must be in English or French or, if in another language, be provided with an English or French translation and a translator’s declaration”. Moreover, the Commentaries to the Refugee Protection Division Rules provide that “document” includes “any correspondence, memorandum, book, plan, map, drawing, diagram, picture or graphic work, photograph, film, microform, sound recording, videotape, machine‑readable record, and any other documentary material, regardless of physical form or characteristics, and any copy of those documents”. Here, the DVD is a “document” that was not translated as required by the Rules. The panel was therefore entitled to attach no probative value to it.

[27] The applicant is forgetting that the finding about the DVD counts for very little among the other things that undermined his credibility with the panel. In particular, the panel found omissions, contradictions between his PIF and his testimony at the hearing and implausibilities in his narrative. It was entitled to draw adverse inferences about his credibility based on all of these factors: Tejeda v. Canada (Minister of Citizenship and Immigration), 2009 FC 421, at paragraph 15.

[28] It is already well established that the Board’s decisions on questions of credibility and assessment of evidence are entitled to great deference by the Court: Zavala v. Canada (Minister of Citizenship and Immigration), 2009 FC 370, at paragraph 5; Mugesera v. Canada (Minister of Citizenship and Immigration), 2005 SCC 40, at paragraph 38. The panel is in the best position to assess the explanations submitted by claimants for any perceived inconsistencies and implausibilities. The role of this Court is not to substitute its judgment for the panel’s findings of fact relating to the credibility of claimants: Martinez v. Canada (Minister of Citizenship and Immigration), 2009 FC 441, at paragraph 11. The Court will intervene only if the panel’s decision does not fall within a range of acceptable and rational solutions (Dunsmuir, at paragraph 47).

[29] In my opinion, the panel’s finding on the applicant’s credibility is not unreasonable in light of the many discrepancies and implausibilities in his testimony.

[30] In his memorandum of argument, the respondent quotes paragraph 4 of Obeng v. Canada (Minister of Citizenship and Immigration), 2004 FC 636, an extract that I find interesting for our purposes:
. . . In Sheikh v. Canada (M.E.I.), [1990] 3 F.C. 238, the Federal Court of Appeal held that a tribunal’s perception that the applicant is not credible on an important aspect of the claim can amount to a finding that there is no credible evidence on which the claim can be based. . . .

[31] Where a panel concludes that a claimant is not credible, it is not obliged to explain everything that supports the allegations that are contrary to the allegations it accepts. It is enough for the panel, as here, to clearly explain why it questions the claimant’s credibility: Luis c. Canada (Ministre de la Citoyenneté et de l’Immigration), 2009 CF 352, at paragraph 22.
Specialized knowledge

[32] The second issue concerns the panel’s “specialized knowledge”. A review of the record shows that the panel drew on its specialized knowledge to explain to the applicant that there are refugee protection claimants who have filed complaints with the Mexican authorities without necessarily being injured or on their deathbed.

[33] The applicant argues that the panel’s “specialized knowledge” had to be based on documentary evidence and that he had to be given that evidence at the time of the hearing so he could respond to it.

[34] In general, the panel must notify the claimant when it intends to use “its specialized knowledge”, as provided for in Rule 18:
18. Before using any information or opinion that is within its specialized knowledge, the Division must notify the claimant or protected person, and the Minister if the Minister is present at the hearing, and give them a chance to
(a) make representations on the reliability and use of the information or opinion; and
(b) give evidence in support of their representations.
18. Avant d'utiliser un renseignement ou une opinion qui est du ressort de sa spécialisation, la Section en avise le demandeur d'asile ou la personne protégée et le ministre -- si celui-ci est présent à l'audience -- et leur donne la possibilité de:
a) faire des observations sur la fiabilité et l'utilisation du renseignement ou de l'opinion;
b) fournir des éléments de preuve à l'appui de leurs observations.

[35] In Isakova v. Canada (Minister of Citizenship and Immigration), Mr. Justice Campbell explained the objective of Rule 18 at paragraph 16 of his reasons:
The purpose of Rule 18 is to enable a claimant to have notice of the specialized knowledge and to give him or her the opportunity to challenge its content and use in reaching a decision. Therefore, in order for Rule 18 to be effective, the RPD member who declares specialized knowledge must place on the record sufficient detail of the knowledge so as to allow it to be tested. That is, the knowledge must be quantifiable and verifiable. As stated by Justice Teitelbaum in Mama v. Canada (Minister of Employment and Immigration), [1994] F.C.J. No. 1515, unverifiable personal knowledge does not qualify as specialized knowledge:
The applicant submits (and I agree), that the personal and/or professional experiences of the Board members, the full extent of which was unclear, hardly justified their claim to “specialized knowledge”. The Board did not purport to take judicial notice of any facts with respect to European border controls and there was no evidence whatsoever before it as to the efficacy of these.
Once the RPD has disclosed its knowledge, Rule 18 then mandates that the RPD allow a claimant to make submissions and present contradictory evidence.

[36] In my opinion, the “specialized knowledge” relied on in this case was mischaracteri

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]


## 22752:2 · paragraphs 39-39

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `b99fb173819c5ef315e52f87424cc0e63001bc604026899a6138da4e70c552a3`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 22752:2:subtheme:1 · paragraphs 39-39

- Raw key terms: `appearances, applicant, attorney, canada, dated, deputy, dung, general`
- Display key terms: `dated, deputy, dung`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: dated, deputy, dung No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 39-39. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT: TEITELBAUM D.J.
DATED: June 4, 2009
APPEARANCES:
Stéphanie Valois
FOR THE APPLICANT
Thi My Dung Tran
FOR THE RESPONDENT
SOLICITORS OF RECORD:
Stéphanie Valois
407 Saint Laurent, Suite 300
Montréal, Quebec
H2Y 2Y5
FOR THE APPLICANT
John H. Sims, Q.C.
Deputy Attorney General of Canada
FOR THE RESPONDENT
