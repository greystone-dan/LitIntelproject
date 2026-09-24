# Discussion Units: case 18729

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **31**
- Continuity pairs: **30**
- Discussion Units: **3**
- Paragraph source hashes: **31**
- Sub-themes: **12**

## 18729:1 · paragraphs 0-27

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `0c97257b1dfac358b23cd15d48cad2787494a6ff92d7b33bb67631526446112f`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 18729:1:subtheme:1 · paragraphs 0-5

- Raw key terms: `applicant, decision, application, canada, found, home, immigration, incident`
- Display key terms: `home, incident`
- Argument roles: `disposition, evidence_fact, governing_rule, party_position`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, party_position Display terms: home, incident Position/evidence statements: Feeling threatened, the Applicant fled Nigeria to come to Canada on November 26, 2007, where he immediately claimed refugee protection. Rule/authority context: [1] This is an application for judicial review pursuant to section 72 of the Immigration and Refugee Protection Act, S. Operative outcome context: [2] For the reasons that follow, I have found that this application for judicial review ought to be dismissed. Evidence spans paragraphs 0-5. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4888711` offsets `47-58`; context: [1] This is an application for judicial review pursuant to section 72 of the Immigration and Refugee Protection Act, S.
- Evidence: `evidence_fact` cue `found that` at chunk `4888712` offsets `40-50`; context: [2] For the reasons that follow, I have found that this application for judicial review ought to be dismissed.
- Evidence: `disposition` cue `dismissed` at chunk `4888712` offsets `100-109`; context: [2] For the reasons that follow, I have found that this application for judicial review ought to be dismissed.
- Evidence: `party_position` cue `claimed` at chunk `4888715` offsets `685-692`; context: Feeling threatened, the Applicant fled Nigeria to come to Canada on November 26, 2007, where he immediately claimed refugee protection.

#### 18729:1:subtheme:2 · paragraphs 6-7

- Raw key terms: `applicant, because, board, claim, credible, found, information, life`
- Display key terms: `because, credible, information, life`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, issue, reasoning_application Display terms: because, credible, information, life Application context: He had added that he believed the PDP thugs and the Nigerian police were looking for him and so he could not attempt to go through the airport in his own name because “the police are everywhere”. | [7] Because of all these implausibilities and contradictions, and because of the Applicant’s tendency to hide or disguise information, the Board found that the cumulative effect of these flaws in the Applicant’s story we Operative outcome context: When asked to explain why the officer would write this, the Applicant first denied having made this statement and later said that he did not know why the Minister’s Delegate had written that in the report. Evidence spans paragraphs 6-7. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4888716` offsets `2295-2302`; context: The Board had concerns as to whether the Applicant had established any significant political profile such that he would be targeted after all this time.
- Evidence: `evidence_fact` cue `testimony` at chunk `4888716` offsets `501-510`; context: The Board found inconsistent the fact that the Applicant wrote in his amended Personal Information Form (“PIF”) that he became actively involved in politics at an early age, before leaving Nigeria, while he stated in his oral testimony that the only early involvement he had was some help he provided to his mother while serving food and drinks to his father’s political associates.
- Evidence: `reasoning_application` cue `because` at chunk `4888716` offsets `4487-4494`; context: He had added that he believed the PDP thugs and the Nigerian police were looking for him and so he could not attempt to go through the airport in his own name because “the police are everywhere”.
- Evidence: `counterargument_limitation` cue `However` at chunk `4888716` offsets `1714-1721`; context: However, the panel was of the opinion that the explanation was implausible in that the only thing that the Applicant identified as being in his area of expertise was that he believed Americans ran elections so that people could obtain power through free and fair process.
- Evidence: `disposition` cue `denied` at chunk `4888716` offsets `5359-5365`; context: When asked to explain why the officer would write this, the Applicant first denied having made this statement and later said that he did not know why the Minister’s Delegate had written that in the report.
- Evidence: `issue` cue `issues` at chunk `4888717` offsets `599-605`; context: The issues
- Evidence: `evidence_fact` cue `found that` at chunk `4888717` offsets `145-155`; context: [7] Because of all these implausibilities and contradictions, and because of the Applicant’s tendency to hide or disguise information, the Board found that the cumulative effect of these flaws in the Applicant’s story were sufficient to conclude that the Applicant’s lack of credibility extends to the totality of his claim.
- Evidence: `reasoning_application` cue `Because` at chunk `4888717` offsets `4-11`; context: [7] Because of all these implausibilities and contradictions, and because of the Applicant’s tendency to hide or disguise information, the Board found that the cumulative effect of these flaws in the Applicant’s story were sufficient to conclude that the Applicant’s lack of credibility extends to the totality of his claim.

#### 18729:1:subtheme:3 · paragraphs 8-9

- Raw key terms: `board, irpa, proof, standard, analysis, applicable, applicant, application`
- Display key terms: `irpa, proof, standard, analysis, applicable`
- Argument roles: `governing_rule, issue, reasoning_application`
- Explanation: Observed roles: governing_rule, issue, reasoning_application Display terms: irpa, proof, standard, analysis, applicable Rule/authority context: What is the applicable standard of review? | [9] The articulation of the correct standard of proof under s. Application context: It is therefore to be reviewed under the correctness standard. Evidence spans paragraphs 8-9. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4888718` offsets `53-59`; context: [8] This application for judicial review raises four issues, which can be summarized as follows:
A.
- Evidence: `governing_rule` cue `standard of review` at chunk `4888718` offsets `123-141`; context: What is the applicable standard of review?
- Evidence: `issue` cue `question` at chunk `4888719` offsets `83-91`; context: 97 of the IRPA is a question of law that goes beyond the expertise of the Board.
- Evidence: `governing_rule` cue `under` at chunk `4888719` offsets `54-59`; context: [9] The articulation of the correct standard of proof under s.
- Evidence: `reasoning_application` cue `therefore` at chunk `4888719` offsets `150-159`; context: It is therefore to be reviewed under the correctness standard.

#### 18729:1:subtheme:4 · paragraphs 10-13

- Raw key terms: `standard, according, applicant, balance, canada, case, citizenship, establish`
- Display key terms: `standard, according, balance, case, establish`
- Argument roles: `governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: governing_rule, issue, party_position, reasoning_application Display terms: standard, according, balance, case, establish Position/evidence statements: [12] The Applicant somewhat confusingly argued that the Board erred in law in applying the test of “more likely than not” to a section 97 determination. Rule/authority context: [11] Finally, the credibility finding is a question of fact that deserves deference and ought to be reviewed under the reasonableness standard: Dunsmuir v. | According to the Applicant, the jurisprudence is to the effect that a claimant has to establish his case on a balance of probabilities, not that the persecution would be more likely than not. Application context: But more importantly, one must distinguish between the standard of proof and the test to be applied under paragraphs 97(1)(a) and (b). Evidence spans paragraphs 10-13. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4888720` offsets `12-18`; context: [10] As for issues of procedural fairness, it is well-established that they are also reviewable according to the correctness standard: Canadian Union of Public Employees (C.
- Evidence: `issue` cue `question` at chunk `4888721` offsets `43-51`; context: [11] Finally, the credibility finding is a question of fact that deserves deference and ought to be reviewed under the reasonableness standard: Dunsmuir v.
- Evidence: `governing_rule` cue `under` at chunk `4888721` offsets `109-114`; context: [11] Finally, the credibility finding is a question of fact that deserves deference and ought to be reviewed under the reasonableness standard: Dunsmuir v.
- Evidence: `party_position` cue `argued` at chunk `4888722` offsets `40-46`; context: [12] The Applicant somewhat confusingly argued that the Board erred in law in applying the test of “more likely than not” to a section 97 determination.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4888722` offsets `185-198`; context: According to the Applicant, the jurisprudence is to the effect that a claimant has to establish his case on a balance of probabilities, not that the persecution would be more likely than not.
- Evidence: `governing_rule` cue `under` at chunk `4888723` offsets `258-263`; context: But more importantly, one must distinguish between the standard of proof and the test to be applied under paragraphs 97(1)(a) and (b).
- Evidence: `reasoning_application` cue `applied` at chunk `4888723` offsets `250-257`; context: But more importantly, one must distinguish between the standard of proof and the test to be applied under paragraphs 97(1)(a) and (b).

#### 18729:1:subtheme:5 · paragraphs 14-16

- Raw key terms: `apparent, applicant, balance, board, cruel, danger, entitled, establish`
- Display key terms: `apparent, balance, cruel, danger, entitled, establish`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: apparent, balance, cruel, danger, entitled, establish Position/evidence statements: [16] Counsel for the Applicant submitted that the Board breached procedural fairness by failing to offer the Applicant an opportunity to confront the apparent significant inconsistency in the fact that the Applicant was  Rule/authority context: [14] As for the legal test to meet in order to establish a danger of torture or a risk to life or to cruel and unusual treatment or punishment, the Federal Court of Appeal has confirmed that it is also the balance of pro | This is clearly the legal test to be applied pursuant to s. Application context: Proof on a balance of probabilities is the standard of proof the panel will apply in assessing the evidence adduced before it for purposes of making its factual findings. | This is clearly the legal test to be applied pursuant to s. Evidence spans paragraphs 14-16. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4888724` offsets `1028-1035`; context: The test for determining the danger of torture is whether, on the facts found by the panel, the panel is satisfied that it is more likely than not that the individual would personally be subjected to a danger of torture.
- Evidence: `evidence_fact` cue `evidence` at chunk `4888724` offsets `906-914`; context: Proof on a balance of probabilities is the standard of proof the panel will apply in assessing the evidence adduced before it for purposes of making its factual findings.
- Evidence: `governing_rule` cue `legal test` at chunk `4888724` offsets `16-26`; context: [14] As for the legal test to meet in order to establish a danger of torture or a risk to life or to cruel and unusual treatment or punishment, the Federal Court of Appeal has confirmed that it is also the balance of probabilities, or more likely than not.
- Evidence: `reasoning_application` cue `apply` at chunk `4888724` offsets `883-888`; context: Proof on a balance of probabilities is the standard of proof the panel will apply in assessing the evidence adduced before it for purposes of making its factual findings.
- Evidence: `counterargument_limitation` cue `nevertheless` at chunk `4888724` offsets `422-434`; context: 97(1) are the same, the concepts are nevertheless distinct.
- Evidence: `evidence_fact` cue `evidence` at chunk `4888725` offsets `402-410`; context: Since the Applicant was found not to be a credible witness and had not advanced any additional credible evidence to suggest he would face any danger, the Board was also clearly entitled to find that he had not met his burden of proof to establish his case on a balance of probabilities.
- Evidence: `governing_rule` cue `legal test` at chunk `4888725` offsets `254-264`; context: This is clearly the legal test to be applied pursuant to s.
- Evidence: `reasoning_application` cue `applied` at chunk `4888725` offsets `271-278`; context: This is clearly the legal test to be applied pursuant to s.
- Evidence: `party_position` cue `submitted` at chunk `4888726` offsets `31-40`; context: [16] Counsel for the Applicant submitted that the Board breached procedural fairness by failing to offer the Applicant an opportunity to confront the apparent significant inconsistency in the fact that the Applicant was self-employed while he claimed to have been living in hiding.
- Evidence: `reasoning_application` cue `therefore` at chunk `4888726` offsets `421-430`; context: At the hearing, counsel added that being self-employed, the Applicant did not have to be physically present at his place of work and could therefore be working while hiding.

#### 18729:1:subtheme:6 · paragraphs 17-19

- Raw key terms: `credibility, applicant, board, evidence, finding, abducted, able, accumulation`
- Display key terms: `credibility, finding, abducted, able, accumulation`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: credibility, finding, abducted, able, accumulation Application context: More importantly, I do not think it was unreasonable for the Board to conclude that the Applicant cannot be said to have been in hiding if he was able to live at the same place from mid-April to November and if he was ab Evidence spans paragraphs 17-19. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Whether` at chunk `4888727` offsets `805-812`; context: Whether he actually had to be physically present to conduct his business or not, the fact remains that this is where he was living without ever moving for more than six months.
- Evidence: `evidence_fact` cue `affidavit` at chunk `4888727` offsets `236-245`; context: It is not entirely clear where the Applicant was kidnapped; his father does not mention this incident in his affidavit, and one of his friends indicated in his affidavit that he was abducted on the highway.
- Evidence: `reasoning_application` cue `conclude` at chunk `4888727` offsets `610-618`; context: More importantly, I do not think it was unreasonable for the Board to conclude that the Applicant cannot be said to have been in hiding if he was able to live at the same place from mid-April to November and if he was able to work as a trader throughout that time.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `4888727` offsets `638-644`; context: More importantly, I do not think it was unreasonable for the Board to conclude that the Applicant cannot be said to have been in hiding if he was able to live at the same place from mid-April to November and if he was able to work as a trader throughout that time.
- Evidence: `evidence_fact` cue `evidence` at chunk `4888728` offsets `130-138`; context: [18] The general lack of credibility finding in the case at bar is based on an accumulation of inconsistencies in the Applicant’s evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `4888729` offsets `220-228`; context: However, the cumulative effect of all of them is that I do not have sufficient credible or trustworthy evidence upon which to base a determination that the claimant is a Convention refugee.
- Evidence: `counterargument_limitation` cue `However` at chunk `4888729` offsets `117-124`; context: However, the cumulative effect of all of them is that I do not have sufficient credible or trustworthy evidence upon which to base a determination that the claimant is a Convention refugee.

#### 18729:1:subtheme:7 · paragraphs 20-21

- Raw key terms: `applicant, board, canada, citizenship, contradictions, immigration, make, minister`
- Display key terms: `contradictions, make`
- Argument roles: `evidence_fact, governing_rule, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, reasoning_application Display terms: contradictions, make Rule/authority context: [19] The jurisprudence recognizes the possibility for a tribunal to make a negative finding based on cumulative credibility concerns: [T]he accumulation of inconsistencies, contradictions, etc. Application context: , taken as a whole, can rightly lead the Board to conclude that an applicant’s credibility is fatally undermined. Evidence spans paragraphs 20-21. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4888730` offsets `9-22`; context: [19] The jurisprudence recognizes the possibility for a tribunal to make a negative finding based on cumulative credibility concerns:
[T]he accumulation of inconsistencies, contradictions, etc.
- Evidence: `reasoning_application` cue `conclude` at chunk `4888730` offsets `243-251`; context: , taken as a whole, can rightly lead the Board to conclude that an applicant’s credibility is fatally undermined.
- Evidence: `evidence_fact` cue `evidence` at chunk `4888731` offsets `356-364`; context: In the present case, the Board reasonably found a number of such contradictions and discrepancies in the Applicant’s evidence.

#### 18729:1:subtheme:8 · paragraphs 22-24

- Raw key terms: `board, canada, citizenship, credibility, immigration, applicant, based, case`
- Display key terms: `credibility, based, case`
- Argument roles: `evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, party_position, reasoning_application Display terms: credibility, based, case Position/evidence statements: The Applicant’s lack of credibility can also be extended to all documentary evidence that he submitted to corroborate his version of the facts. | [23] The Applicant also submitted that the Board erred by concluding that his documents were false solely because forged documents are widely available in Nigeria. Application context: [23] The Applicant also submitted that the Board erred by concluding that his documents were false solely because forged documents are widely available in Nigeria. Evidence spans paragraphs 22-24. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4888732` offsets `49-57`; context: [21] Furthermore, the Board is also justified to question a claimant’s credibility based on common sense, implausibility and rationality inherent to his story: Kiyarath v.
- Evidence: `party_position` cue `submitted` at chunk `4888733` offsets `475-484`; context: The Applicant’s lack of credibility can also be extended to all documentary evidence that he submitted to corroborate his version of the facts.
- Evidence: `evidence_fact` cue `evidence` at chunk `4888733` offsets `235-243`; context: Such a general finding of lack of credibility extends to all relevant evidence emanating from the Applicant’s version: Sheikh v.
- Evidence: `party_position` cue `submitted` at chunk `4888734` offsets `24-33`; context: [23] The Applicant also submitted that the Board erred by concluding that his documents were false solely because forged documents are widely available in Nigeria.
- Evidence: `evidence_fact` cue `testimony` at chunk `4888734` offsets `824-833`; context: 255, the Board took into consideration the availability of false documents and the general lack of credibility of the Applicant’s testimony before concluding, not that the documents were forged, but that they must be given little weight.
- Evidence: `reasoning_application` cue `because` at chunk `4888734` offsets `106-113`; context: [23] The Applicant also submitted that the Board erred by concluding that his documents were false solely because forged documents are widely available in Nigeria.

#### 18729:1:subtheme:9 · paragraphs 25-26

- Raw key terms: `applicant, board, court, credibility, effect, account, addition, admitted`
- Display key terms: `credibility, effect, account, addition, admitted`
- Argument roles: `disposition, evidence_fact, issue, party_position`
- Explanation: Observed roles: disposition, evidence_fact, issue, party_position Display terms: credibility, effect, account, addition, admitted Position/evidence statements: [24] Finally, the Applicant argued that the Board erroneously drew a negative inference from the fact that the Applicant amended his PIF to add his two children whom he previously failed to declare. Operative outcome context: The Board reasonably dismissed his submission to the effect that he never made such a statement and preferred the officer’s notes. Evidence spans paragraphs 25-26. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4888735` offsets `419-424`; context: Indeed, it was not the amendment of the PIF that led the Board to draw a negative inference; rather, it was the recurrent misrepresentation of the truth by the Applicant that raised an issue in the Board member’s mind.
- Evidence: `party_position` cue `argued` at chunk `4888735` offsets `28-34`; context: [24] Finally, the Applicant argued that the Board erroneously drew a negative inference from the fact that the Applicant amended his PIF to add his two children whom he previously failed to declare.
- Evidence: `disposition` cue `dismissed` at chunk `4888735` offsets `1190-1199`; context: The Board reasonably dismissed his submission to the effect that he never made such a statement and preferred the officer’s notes.
- Evidence: `evidence_fact` cue `evidence` at chunk `4888736` offsets `21-29`; context: [25] In light of the evidence that was before the Board, it was reasonable for it to make a general finding of lack of credibility based on the cumulative effect of contradictions, implausibilities and discrepancies in the Applicant’s story.

#### 18729:1:subtheme:10 · paragraphs 27-27

- Raw key terms: `application, certification, certified, dismissed, foregoing, judicial, neither, none`
- Display key terms: `certification, certified, dismissed, foregoing, judicial, neither, none`
- Argument roles: `disposition, issue`
- Explanation: Observed roles: disposition, issue Display terms: certification, certified, dismissed, foregoing, judicial, neither, none Operative outcome context: [26] For all the foregoing reasons, the application for judicial review is dismissed. Evidence spans paragraphs 27-27. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4888737` offsets `111-119`; context: Neither party proposed a question for certification, and none will be certified.
- Evidence: `disposition` cue `dismissed` at chunk `4888737` offsets `75-84`; context: [26] For all the foregoing reasons, the application for judicial review is dismissed.

#### Section text

Lawal v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2010-05-21
Neutral citation
2010 FC 558
File numbers
IMM-5102-09
Decision Content
Federal Court
Cour fédérale
Date: 20100521
Docket: IMM-5102-09
Citation: 2010 FC 558
Ottawa, Ontario, May 21, 2010
PRESENT: The Honourable Mr. Justice de Montigny
BETWEEN:
SAMSON LAWAL
Applicant
and
THE MINISTER OF CITIZENSHIP
AND IMMIGRATION
Respondent
REASONS FOR ORDER AND ORDER

[1] This is an application for judicial review pursuant to section 72 of the Immigration and Refugee Protection Act, S.C. 2001, c. 27 (the “IRPA”) of a decision by the Refugee Protection Division of the Immigration and Refugee Board (the “Board”) dated September 23, 2009, wherein the Applicant’s refugee claim was rejected.

[2] For the reasons that follow, I have found that this application for judicial review ought to be dismissed.
I. The facts

[3] The Applicant is a 44 year old Nigerian citizen who left his home country in 1991 to visit the United States of America (the “U.S.”). He did not return to Nigeria until he was deported in 2007, after becoming an illegal resident of the U.S. in 2003.

[4] While in the U.S., the Applicant fathered four children with a common-law spouse with whom he lived from 1993 to 2005. In 1997, he was found guilty of forgery and fraud in the U.S. and was sentenced to five years probation, which he served without further incident.

[5] Soon after his return to Nigeria in February 2007, the Applicant alleged that he joined his father in his involvement with the political party Action Congress (“AC”) as an organizer. The Applicant alleged that on April 13, 2007, the family home was burned by thugs associated with the ruling People’s Democratic Party (the “PDP”) during the absence of the Applicant. His sister would have died in the fire. The Applicant also alleged that two days later he was kidnapped and tortured for two days by PDP thugs. The police did not do anything when he reported the incident. Feeling threatened, the Applicant fled Nigeria to come to Canada on November 26, 2007, where he immediately claimed refugee protection. To enter Canada, the Applicant used an admittedly fraudulent U.S. passport in the name of “Vincent Curry”. The Applicant also alleged that his father fled political persecution by moving to South Africa. Finally, the Applicant claimed that he was informed by friends in March 2009 that the police are now looking for him as an alleged member of the Oodua People’s Congress (the “OPC”).
II. The impugned decision

[6] The Board rejected the Applicant’s claim in this case after finding him not credible. According to the reasons issued by the Board, there were numerous implausible and inconsistent statements made by the Applicant. The discrepancies noted by the Board are as follows:
A. The Board found inconsistent the fact that the Applicant wrote in his amended Personal Information Form (“PIF”) that he became actively involved in politics at an early age, before leaving Nigeria, while he stated in his oral testimony that the only early involvement he had was some help he provided to his mother while serving food and drinks to his father’s political associates.
B. Also regarding his family’s political activity, he explained in his revised PIF that his father supported the late Chief Awolowo when the National party of Nigeria (NPN) cheated Awolowo out of the presidency in 1978. At the hearing, when asked about the party his father supported at the gatherings at the family home, he replied that it was the NPN, and specifically clarified that he was referring to the National Party of Nigeria.
C. The Board questioned the Applicant’s involvement in the 2007 election campaign by the AC. The Board found implausible that the Applicant returned to Nigeria in February, joined the AC in March, and then became an organizer and a speaker at rallies for the state election in Lagos scheduled for April 14, 2007 and for the federal positions, scheduled for April 21, 2007. The Board questioned the party’s rush to appoint a recently arrived member to a leader’s position. The Applicant’s explanation was that he had supported the party financially in 2006 and that the party was interested in his American experiences. However, the panel was of the opinion that the explanation was implausible in that the only thing that the Applicant identified as being in his area of expertise was that he believed Americans ran elections so that people could obtain power through free and fair process. However, this would not be news to even moderately informed Nigerians and would not likely be of significant interest during the intensity of an election in Nigeria. The Board also noted that the Applicant did not provide any evidence of his alleged financial support in 2006.
D. The Board had concerns as to whether the Applicant had established any significant political profile such that he would be targeted after all this time. The Applicant’s explanation was that he would be targeted as this is typical of Nigerian politics. When it was pointed out to him that the PDP thugs could not and do not kill all those who support the AC, the Applicant replied that his father had a high profile, his family house had been burned and he had gone to the police to seek protection. The Board, however, noted that the Applicant’s father’s political profile would not make the Applicant a target, especially so soon after he returned from being away for 16 years. Rather, it was reasonable to assume that his father would be a target. Also, given the notorious corruption and inefficiencies of the Nigerian police, the Applicant’s action in reporting his troubles to the police would be no threat to the PDP thugs in Lagos.3
E. The Board noted that a review of the PIF narrative would lead one to believe that the Applicant was kidnapped for two days from the family home. However, the affidavit the Applicant submitted referred to his being “traced and abducted on the highway…[where] he was beaten and abandoned”.
F. The Applicant had alleged in his PIF narrative that after the family house was burned, he was kidnapped when the thugs “came back some few days later”. Yet, he had also alleged that he moved to Freemen Street in Lagos on April 14 and remained living there until he left Nigeria. Of equal significance is the fact that he had also asserted that he worked as a self-employed trader from February 30 until November 1, 2007 in Lagos. The RPD noted that the Applicant’s oral testimony was inconsistent with what he had stated in his PIF. The Applicant had said specifically that he had been kidnapped on April 15 and that he began thinking of leaving Nigeria in mid-May.
G. Given that he already possessed a Nigerian passport, he was asked why he had not simply left the country at that time. The Applicant replied he was in hiding. He had added that he believed the PDP thugs and the Nigerian police were looking for him and so he could not attempt to go through the airport in his own name because “the police are everywhere”. The RPD, however, noted that if the Applicant was able to live at the same place from mid-April to November, and if he was able to work as a trader throughout that time, he could not be said to have been in hiding.
H. Although technically the Applicant made his refugee claim at the port of entry, this was because he had been confronted about his fraudulent travel document before he left the plane. In fact, the Minister’s Delegate Notes before the Board stated:
“Subject was intercepted by members of the disembarkation team who had concerns about the validity of the American passport in his possession. He admitted during this review process that if he had entered Canada undetected, he would have travelled to the United States to attempt entry there”.
When asked to explain why the officer would write this, the Applicant first denied having made this statement and later said that he did not know why the Minister’s Delegate had written that in the report. The Board preferred the statement made by the immigration officer to the testimony of the Applicant who had shown by past behaviour a willingness to distort the truth. The immigration officer also noted that the Applicant stated being widowed and having two children at the port of entry, while he indicated being never married and having two children in his first PIF. The Applicant finally amended his PIF to declare having four children and testified orally that he has been in a common-law marriage for 12 years. The Board found that the Applicant gave no reasonable explanation for these discrepancies.
I. The Board found concerning the fact that the Applicant stated that when he went to the U.S. in 1991, he intended to return to Nigeria after a few months visit. However, he stayed there for 16 years, with no legal status during the last three of them, and said that he did not know why he did so. The panel found this answer troubling, because it either indicated that the Applicant had failed to reflect upon an important life decision or that he was withholding an important life decision or that he was withholding an answer because he feared the consequences or disapproval from the tribunal.
J. The serious criminal conviction in the U.S. for forgery and fraud, although not serious enough to warrant exclusion, was taken into account by the Board as an indication of the Applicant’s willingness to misrepresent the truth to serve his own desires.
K. The Board found implausible the Applicant’s amended PIF as he claimed that the Nigerian police had accused him of being a member of the OPC. The Board explained that with the degree of corruption in Nigeria, the police do not need to accuse him of being a member of a party in order to detain him with relative impunity. Furthermore, although the Board was willing to believe that the police may not offer protection to people persecuted by the PDP thugs, there is no evidence that the police would seek to persecute him for their own reasons.
L. The Board recognized that the Applicant provided some documentary evidence supporting some of his alleged problems in Nigeria. However, the Board relied on a Norwegian fact-finding report and found that fraudulent documents and genuine documents with false information are widely available in Nigeria. Therefore, the Board gave the documents little weight.

[7] Because of all these implausibilities and contradictions, and because of the Applicant’s tendency to hide or disguise information, the Board found that the cumulative effect of these flaws in the Applicant’s story were sufficient to conclude that the Applicant’s lack of credibility extends to the totality of his claim. The Board therefore concluded, on a balance of probabilities, that the Applicant is not a credible witness and that he is not a person who more likely than not, faces a risk to his life or a risk of cruel and unusual treatment or punishment if returned to Nigeria.
III. The issues

[8] This application for judicial review raises four issues, which can be summarized as follows:
A. What is the applicable standard of review?
B. Did the Board err in law in regard of the standard of proof applicable under section 7 of the IRPA?
C. Did the Board breach procedural fairness by failing to confront the Applicant with its concern regarding the contradiction between the stability of his employment and housing during a period in which he declared to be in hiding?
D. Did the Board err in it finding of general lack of credibility?
IV. Analysis
A. The Applicable Standard ff Review

[9] The articulation of the correct standard of proof under s. 97 of the IRPA is a question of law that goes beyond the expertise of the Board. It is therefore to be reviewed under the correctness standard.

[10] As for issues of procedural fairness, it is well-established that they are also reviewable according to the correctness standard: Canadian Union of Public Employees (C.U.P.E.) v. Ontario (Minister of Labour), 2003 SCC 29, [2003] S.C.J. No. 28 at para. 100; Sketchley v. Canada (Attorney General), 2005 FCA 404, [2005] F.C.J. No. 2056 at para. 54; Guo v. Canada (Minister of Citizenship and Immigration) (1996), 65 A.C.W.S. (3d) 991 (F.C.T.D.) at para. 2

[11] Finally, the credibility finding is a question of fact that deserves deference and ought to be reviewed under the reasonableness standard: Dunsmuir v. New Brunswick, 2008 SCC 9, [2008] S.C.J. No. 9 at para. 53; Aguebor v. Canada (Minister of Employment and Immigration) (1993), 42 A.C.W.S. (3d) 886, at para. 4 (F.C.A.); Gatore v. Canada (Minister of Citizenship and Immigration), 2009 FC 702, [2009] F.C.J. No. 871 at paras. 27-28.
B. The Standard of Proof Under Section 97

[12] The Applicant somewhat confusingly argued that the Board erred in law in applying the test of “more likely than not” to a section 97 determination. According to the Applicant, the jurisprudence is to the effect that a claimant has to establish his case on a balance of probabilities, not that the persecution would be more likely than not.

[13] This argument is clearly without merit. First of all, there is no distinction between the balance of probabilities and the “more likely than not” tests. But more importantly, one must distinguish between the standard of proof and the test to be applied under paragraphs 97(1)(a) and (b). Unless the words of a statute or the context requires otherwise, the standard of proof in civil cases is always proof on a balance of probabilities. Accordingly, an applicant will have to establish his case on a balance of probabilities with respect both to sections 96 and 97.

[14] As for the legal test to meet in order to establish a danger of torture or a risk to life or to cruel and unusual treatment or punishment, the Federal Court of Appeal has confirmed that it is also the balance of probabilities, or more likely than not. This is true for both paragraphs 97(1)(a) and (b). While the words used to describe the standard of proof and the test under s. 97(1) are the same, the concepts are nevertheless distinct. As the Court stated:
It is immediately apparent that the words used to describe the standard of proof – balance of probabilities – are equivalent to the words used to describe the legal test to be met in order to be entitled to protection under paragraph 97(1)(a) – more likely than not. Although the words are equivalent, there are two distinct steps involved. Proof on a balance of probabilities is the standard of proof the panel will apply in assessing the evidence adduced before it for purposes of making its factual findings. The test for determining the danger of torture is whether, on the facts found by the panel, the panel is satisfied that it is more likely than not that the individual would personally be subjected to a danger of torture.
Li v. Canada (Minister of Citizenship and Immigration), 2005 FCA 1, [2005] F.C.J. No. 1 at para. 29.

[15] In the case at bar, the Board made no mistake in finding that the claimant is not a person who more likely than not faces a risk to his life or a risk of cruel and unusual treatment or punishment if he were to return to Nigeria. This is clearly the legal test to be applied pursuant to s. 97. Since the Applicant was found not to be a credible witness and had not advanced any additional credible evidence to suggest he would face any danger, the Board was also clearly entitled to find that he had not met his burden of proof to establish his case on a balance of probabilities.
C. Procedural Fairness

[16] Counsel for the Applicant submitted that the Board breached procedural fairness by failing to offer the Applicant an opportunity to confront the apparent significant inconsistency in the fact that the Applicant was self-employed while he claimed to have been living in hiding. At the hearing, counsel added that being self-employed, the Applicant did not have to be physically present at his place of work and could therefore be working while hiding.

[17] I agree with the Respondent that the Board had no duty to confront the Applicant with obvious discrepancies in his story. It is not entirely clear where the Applicant was kidnapped; his father does not mention this incident in his affidavit, and one of his friends indicated in his affidavit that he was abducted on the highway. Yet, a natural reading of the PIF narrative would lead one to believe the applicant was kidnapped for two days from the family home (as the Applicant seems to suggest by saying that the thugs “came back”). More importantly, I do not think it was unreasonable for the Board to conclude that the Applicant cannot be said to have been in hiding if he was able to live at the same place from mid-April to November and if he was able to work as a trader throughout that time. Whether he actually had to be physically present to conduct his business or not, the fact remains that this is where he was living without ever moving for more than six months.
D. The Adverse Credibility Finding

[18] The general lack of credibility finding in the case at bar is based on an accumulation of inconsistencies in the Applicant’s evidence. In its credibility conclusion, the Board wrote:

[33] I am aware that none of the credibility concerns raised here may be sufficient on its own to negate this claim. However, the cumulative effect of all of them is that I do not have sufficient credible or trustworthy evidence upon which to base a determination that the claimant is a Convention refugee.

[19] The jurisprudence recognizes the possibility for a tribunal to make a negative finding based on cumulative credibility concerns:
[T]he accumulation of inconsistencies, contradictions, etc., taken as a whole, can rightly lead the Board to conclude that an applicant’s credibility is fatally undermined.
Asashi v. Canada (Minister of Citizenship and Immigration), 2005 FC 102, [2005] F.C.J. No. 129 at para. 8.

[20] Indeed, the Board is entitled to make negative inferences from repeated internal contradictions and discrepancies in an applicant’s story: Kilola v. Canada (Minister of Citizenship and Immigration), [2000] 185 F.T.R. 124 at para. 18. In the present case, the Board reasonably found a number of such contradictions and discrepancies in the Applicant’s evidence. As the Federal Court of Appeal once stated:
[u]nless one is prepared to postulate (and accept) unlimited credulity on the part of the Board, there must come a point at which a witness’ contradictions will move even the most generous trier of fact to reject his evidence.
Canada (Minister of Employment and Immigration) v. Dan-Ash (1988), 5 Imm. L.R. (2d) 78 (F.C.A); see also Perjaku v. Canada (Minister of Citizenship and Immigration), 2007 FC 496, [2007] F.C.J. No. 669 at para. 18.

[21] Furthermore, the Board is also justified to question a claimant’s credibility based on common sense, implausibility and rationality inherent to his story: Kiyarath v. Canada (Minister of Citizenship and Immigration), 2005 FC 1269, [2005] F.C.J. No. 1529 at para. 22; Osakpolo v. Canada (Minister of Citizenship and Immigration), 2009 FC 286, [2009] F.C.J. No. 381 at para. 39; Shahamati v. Canada (Minister of Employment and Immigration), [1994] F.C.J. No. 415 (F.C.A.).

[22] Given all the inconsistencies and implausibilities listed above, it was reasonable for the Board to make a general finding of lack of credibility in this case. Such a general finding of lack of credibility extends to all relevant evidence emanating from the Applicant’s version: Sheikh v. Canada (Ministry of Employment and Immigration), [1990] 3 F.C. 238 at para. 8 (F.C.A.). The Applicant’s lack of credibility can also be extended to all documentary evidence that he submitted to corroborate his version of the facts. As a result, the Board did not have to consider all of the documentary evidence in support of the Applicant’s story: Nijjer v. Canada (Ministry of Citizensh

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]


## 18729:2 · paragraphs 28-29

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `9f804e78810d9060be1912f21dd97736350a2eda906d4f2d54d3933c1fbe9088`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 18729:2:subtheme:1 · paragraphs 28-29

- Raw key terms: `application, cause, certification, court, date, dismissed, docket, federal`
- Display key terms: `certification, date, dismissed, federal`
- Argument roles: `disposition, issue`
- Explanation: Observed roles: disposition, issue Display terms: certification, date, dismissed, federal Operative outcome context: ORDER THIS COURT ORDERS that the application for judicial review is dismissed. Evidence spans paragraphs 28-29. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4888737` offsets `258-266`; context: There is no question for certification.
- Evidence: `disposition` cue `dismissed` at chunk `4888737` offsets `235-244`; context: ORDER
THIS COURT ORDERS that the application for judicial review is dismissed.

#### Section text

ORDER
THIS COURT ORDERS that the application for judicial review is dismissed. There is no question for certification.
"Yves de Montigny"
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET: IMM-5102-09
STYLE OF CAUSE: Samson Lawal
v.
MCI
PLACE OF HEARING: Toronto, Ontario
DATE OF HEARING: May 13, 2010
REASONS FOR 

## 18729:3 · paragraphs 30-30

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `c6461afb4481fdba4445196c8412bcfb555053965b13e89f83bc796736d857aa`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 18729:3:subtheme:1 · paragraphs 30-30

- Raw key terms: `adelaide, appearances, applicant, attorney, barrister, briscoe, canada, dated`
- Display key terms: `adelaide, barrister, briscoe, dated`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: adelaide, barrister, briscoe, dated No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 30-30. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

ORDER
AND ORDER BY: de MONTIGNY J.
DATED: May 21, 2010
APPEARANCES:
Sina Ogunleye
FOR THE APPLICANT
Leanne Briscoe
FOR THE RESPONDENT
SOLICITORS OF RECORD:
Barrister & Solicitor
112 Adelaide Street East, 3rd Floor
Toronto, Ontario M5C 1K9
FOR THE APPLICANT
Myles J. Kirvan
Deputy Attorney General of Canada
FOR THE RESPONDENT
