# Discussion Units: case 26003

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **38**
- Continuity pairs: **37**
- Discussion Units: **2**
- Paragraph source hashes: **38**
- Sub-themes: **7**

## 26003:1 · paragraphs 0-36

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `ec59912157ae5aeb4bd47ff8ef796931fc730d7ca786a7e608a7d24bd19eb64a`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 26003:1:subtheme:1 · paragraphs 0-2

- Raw key terms: `applicant, benancio, board, canada, corado, decision, guerrero, immigration`
- Display key terms: `benancio, corado, guerrero`
- Argument roles: `disposition, governing_rule, party_position`
- Explanation: Observed roles: disposition, governing_rule, party_position Display terms: benancio, corado, guerrero Position/evidence statements: [2] The applicant submits that the Board (1) erred in misstating or misconstruing the nature of the risk he faced, thus rendering its analysis invalid, and (2) erred in determining that he did not face a personal risk pu Rule/authority context: He sought protection in Canada as a Convention refugee under s. | [2] The applicant submits that the Board (1) erred in misstating or misconstruing the nature of the risk he faced, thus rendering its analysis invalid, and (2) erred in determining that he did not face a personal risk pu Operative outcome context: His claims were dismissed by the Refugee Protection Division of the Immigration and Refugee Board in its decision of February 28, 2011. Evidence spans paragraphs 0-2. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `under` at chunk `5222717` offsets `111-116`; context: He sought protection in Canada as a Convention refugee under s.
- Evidence: `disposition` cue `dismissed` at chunk `5222717` offsets `251-260`; context: His claims were dismissed by the Refugee Protection Division of the Immigration and Refugee Board in its decision of February 28, 2011.
- Evidence: `party_position` cue `submits` at chunk `5222718` offsets `18-25`; context: [2] The applicant submits that the Board (1) erred in misstating or misconstruing the nature of the risk he faced, thus rendering its analysis invalid, and (2) erred in determining that he did not face a personal risk pursuant to s.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5222718` offsets `218-229`; context: [2] The applicant submits that the Board (1) erred in misstating or misconstruing the nature of the risk he faced, thus rendering its analysis invalid, and (2) erred in determining that he did not face a personal risk pursuant to s.

#### 26003:1:subtheme:2 · paragraphs 3-8

- Raw key terms: `applicant, board, guatemala, decision, error, evidence, fact, facts`
- Display key terms: `guatemala, error, fact, facts`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, reasoning_application Display terms: guatemala, error, fact, facts Rule/authority context: [3] The issues in this case are questions of mixed fact and law are therefore reviewable under the standard of reasonableness: Dunsmuir v New Brunswick, 2008 SCC 9. | [4] This application must be allowed and the Board’s decision that the applicant was not a person in need of protection under s. Application context: [3] The issues in this case are questions of mixed fact and law are therefore reviewable under the standard of reasonableness: Dunsmuir v New Brunswick, 2008 SCC 9. | This error led the Board to unreasonably conclude that the risk faced by the applicant was one faced generally by others in Guatemala. Operative outcome context: [4] This application must be allowed and the Board’s decision that the applicant was not a person in need of protection under s. Evidence spans paragraphs 3-8. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5222719` offsets `8-14`; context: [3] The issues in this case are questions of mixed fact and law are therefore reviewable under the standard of reasonableness: Dunsmuir v New Brunswick, 2008 SCC 9.
- Evidence: `governing_rule` cue `under` at chunk `5222719` offsets `89-94`; context: [3] The issues in this case are questions of mixed fact and law are therefore reviewable under the standard of reasonableness: Dunsmuir v New Brunswick, 2008 SCC 9.
- Evidence: `reasoning_application` cue `therefore` at chunk `5222719` offsets `68-77`; context: [3] The issues in this case are questions of mixed fact and law are therefore reviewable under the standard of reasonableness: Dunsmuir v New Brunswick, 2008 SCC 9.
- Evidence: `governing_rule` cue `under` at chunk `5222720` offsets `120-125`; context: [4] This application must be allowed and the Board’s decision that the applicant was not a person in need of protection under s.
- Evidence: `reasoning_application` cue `conclude` at chunk `5222720` offsets `410-418`; context: This error led the Board to unreasonably conclude that the risk faced by the applicant was one faced generally by others in Guatemala.
- Evidence: `disposition` cue `allowed` at chunk `5222720` offsets `29-36`; context: [4] This application must be allowed and the Board’s decision that the applicant was not a person in need of protection under s.
- Evidence: `evidence_fact` cue `evidence` at chunk `5222721` offsets `225-233`; context: Critically, the recitation of facts by the Board, in some instances, fails to include significant facts from the applicant’s evidence and, in other instances, includes alleged “facts” that are not supported by the record.
- Evidence: `counterargument_limitation` cue `fails` at chunk `5222721` offsets `169-174`; context: Critically, the recitation of facts by the Board, in some instances, fails to include significant facts from the applicant’s evidence and, in other instances, includes alleged “facts” that are not supported by the record.
- Evidence: `evidence_fact` cue `testimony` at chunk `5222722` offsets `134-143`; context: [6] The following summary of the key events is taken from the applicant’s amended Personal Information Form narrative (PIF), his oral testimony before the Board, and the Exhibits accepted by the Board.

#### 26003:1:subtheme:3 · paragraphs 9-26

- Raw key terms: `applicant, board, grandmother, drugs, lorenzanas, organization, border, death`
- Display key terms: `grandmother, drugs, lorenzanas, organization, border, death`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: grandmother, drugs, lorenzanas, organization, border, death Rule/authority context: ” He continued his testimony saying that “I was able to throw myself on the ground and when I rolled to her she was dead under the table and I ran away. | [22] The Board analysed its view of the applicant’s risk under s. Application context: ” The applicant responded that he would not do that because he was studying and he did not want to quit school. | He was directed to get into an SUV because someone wanted to talk to him. Evidence spans paragraphs 9-26. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5222725` offsets `614-621`; context: The man said that he would have to do it whether he wanted to or not.
- Evidence: `reasoning_application` cue `because` at chunk `5222725` offsets `513-520`; context: ” The applicant responded that he would not do that because he was studying and he did not want to quit school.
- Evidence: `reasoning_application` cue `because` at chunk `5222727` offsets `249-256`; context: He was directed to get into an SUV because someone wanted to talk to him.
- Evidence: `evidence_fact` cue `testimony` at chunk `5222728` offsets `454-463`; context: ” He continued his testimony saying that “I was able to throw myself on the ground and when I rolled to her she was dead under the table and I ran away.
- Evidence: `governing_rule` cue `under` at chunk `5222728` offsets `556-561`; context: ” He continued his testimony saying that “I was able to throw myself on the ground and when I rolled to her she was dead under the table and I ran away.
- Evidence: `counterargument_limitation` cue `Although` at chunk `5222728` offsets `589-597`; context: ” Although a careful review of the certified tribunal record suggests some contradictions concerning the details of this engagement, it is uncontested that his grandmother was shot multiple times.
- Evidence: `evidence_fact` cue `record` at chunk `5222729` offsets `469-475`; context: ” Notwithstanding the Board’s colourful description of the recruiting tactics of Los Lorenzanas, there is nothing in the record to support its statement that the applicant was offered money, membership or guns.
- Evidence: `counterargument_limitation` cue `Notwithstanding` at chunk `5222729` offsets `350-365`; context: ” Notwithstanding the Board’s colourful description of the recruiting tactics of Los Lorenzanas, there is nothing in the record to support its statement that the applicant was offered money, membership or guns.
- Evidence: `evidence_fact` cue `evidence` at chunk `5222730` offsets `242-250`; context: The evidence before the Board was that Los Lorenzanas specifically targeted the applicant to work for them to carry drugs across the border, not merely to join their organization, as the Board states.
- Evidence: `reasoning_application` cue `I find` at chunk `5222731` offsets `220-226`; context: [15] Further, although the Board at paragraph 24 finds that the grandmother’s shooting was in retaliation for the applicant refusing the recruitment by Los Lorenzanas, at paragraph 28 of its decision, the Board writes: “I find that the grandmother was harmed incidentally and not as a means to recruit the claimant” [emphasis added].
- Evidence: `evidence_fact` cue `testimony` at chunk `5222732` offsets `83-92`; context: [16] Also perverse is the Board’s finding that her death was “incidental” when the testimony of the applicant, supported by the evidence of the police report and the previous threats, was that they shot at her.
- Evidence: `reasoning_application` cue `conclude` at chunk `5222732` offsets `608-616`; context: Given the 11 bullet wounds in the grandmother’s body, it is unreasonable to conclude that the grandmother’s wounds were “incidental.
- Evidence: `counterargument_limitation` cue `but` at chunk `5222732` offsets `312-315`; context: As is noted above, the applicant in his PIF did state that the killers “started firing at the house” but this must be considered in the context of all the evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `5222735` offsets `32-40`; context: [19] In its appreciation of the evidence, the Board also considered a letter the applicant received from his two friends, Jorge and Byron, with whom he was walking when he was initially approached by a member of Los Lorenzanas, and with whom he had stayed in contact.
- Evidence: `evidence_fact` cue `record` at chunk `5222736` offsets `141-147`; context: [20] The Board is in error in its description of the content of the friends’ letter which can be found on page 293 of the certified tribunal record.
- Evidence: `counterargument_limitation` cue `however` at chunk `5222736` offsets `559-566`; context: The applicant’s friends do however write that they believe that Los Lorenzanas hired Mara 18 to find and kill him.
- Evidence: `evidence_fact` cue `found that` at chunk `5222737` offsets `15-25`; context: [21] The Board found that the harm the applicant feared was “criminality (recruitment to deliver drugs)” and that this was not linked to a Convention ground in s.
- Evidence: `counterargument_limitation` cue `but` at chunk `5222737` offsets `476-479`; context: Further, if there was recruitment, it was not to join Los Lorenzanas but to transport drugs for them.
- Evidence: `evidence_fact` cue `found that` at chunk `5222738` offsets `960-970`; context: ” Notwithstanding its finding that the applicant was targeted, the Board found that the risk he faced was a generalized one, given the pervasiveness of gangs in Guatemala.
- Evidence: `governing_rule` cue `under` at chunk `5222738` offsets `57-62`; context: [22] The Board analysed its view of the applicant’s risk under s.
- Evidence: `reasoning_application` cue `because` at chunk `5222738` offsets `276-283`; context: The Board then noted that the applicant was a prime target for recruitment because of his vulnerable age and social profile.
- Evidence: `counterargument_limitation` cue `Notwithstanding` at chunk `5222738` offsets `889-904`; context: ” Notwithstanding its finding that the applicant was targeted, the Board found that the risk he faced was a generalized one, given the pervasiveness of gangs in Guatemala.
- Evidence: `governing_rule` cue `under` at chunk `5222740` offsets `86-91`; context: [24] This finding is dispositive of the application for judicial review; the decision under review is unreasonable and the applicant’s claim for protection must be redetermined.
- Evidence: `counterargument_limitation` cue `Nevertheless` at chunk `5222740` offsets `178-190`; context: Nevertheless, I wish to add a few comments concerning s.
- Evidence: `evidence_fact` cue `found that` at chunk `5222742` offsets `131-141`; context: [26] Parsing this provision, it is evident that if a claimant is to be found to be a person in need of protection, then it must be found that:
a.

#### 26003:1:subtheme:4 · paragraphs 27-30

- Raw key terms: `claimant, decision-maker, risk, claim, faced, state, actually, analysis`
- Display key terms: `decision-maker, risk, faced, state, actually, analysis`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: decision-maker, risk, faced, state, actually, analysis Position/evidence statements: [30] The Court of Appeal in Sanchez v Canada (Minister of Citizenship and Immigration), 2007 FCA 99, at para 15, cited in Prophète v Canada (Minister of Citizenship and Immigration), 2009 FCA 31, at para 7, stated that “ Rule/authority context: [29] An example of the sort of decision I am addressing is that under review. | [30] The Court of Appeal in Sanchez v Canada (Minister of Citizenship and Immigration), 2007 FCA 99, at para 15, cited in Prophète v Canada (Minister of Citizenship and Immigration), 2009 FCA 31, at para 7, stated that “ Application context: It is important that a decision-maker finds that a claimant has a personal risk because if there is no personal risk to the claimant, then there is no need to do any further analysis of the claim; there is simply no risk Evidence spans paragraphs 27-30. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5222743` offsets `35-42`; context: [27] The majority of cases turn on whether or not the last condition has been satisfied, that is, whether the risk faced by the claimant is a risk faced generally by others in the country.
- Evidence: `reasoning_application` cue `because` at chunk `5222743` offsets `729-736`; context: It is important that a decision-maker finds that a claimant has a personal risk because if there is no personal risk to the claimant, then there is no need to do any further analysis of the claim; there is simply no risk.
- Evidence: `issue` cue `whether` at chunk `5222744` offsets `376-383`; context: ” Before determining whether the risk faced by the claimant is one generally faced by others in the country, the decision-maker must (1) make an express determination of what the claimant’s risk is, (2) determine whether that risk is a risk to life or a risk of cruel and unusual treatment or punishment, and (3) clearly
express the basis for that risk.
- Evidence: `governing_rule` cue `under` at chunk `5222745` offsets `64-69`; context: [29] An example of the sort of decision I am addressing is that under review.
- Evidence: `counterargument_limitation` cue `But` at chunk `5222745` offsets `296-299`; context: ” But this is not the risk faced by the applicant, and even if it were, the decision fails to state how this meets the test of risk set out in subparagraph 97(1)(b)(ii) of the Act.
- Evidence: `party_position` cue `claim` at chunk `5222746` offsets `243-248`; context: [30] The Court of Appeal in Sanchez v Canada (Minister of Citizenship and Immigration), 2007 FCA 99, at para 15, cited in Prophète v Canada (Minister of Citizenship and Immigration), 2009 FCA 31, at para 7, stated that “[t]he examination of a claim under subsection 97(1) of the Act necessitates an individualized inquiry, which is to be conducted on the basis of the evidence adduced by a claimant ‘in the context of a present or prospective risk’ for him” [emphasis in original].
- Evidence: `evidence_fact` cue `evidence` at chunk `5222746` offsets `368-376`; context: [30] The Court of Appeal in Sanchez v Canada (Minister of Citizenship and Immigration), 2007 FCA 99, at para 15, cited in Prophète v Canada (Minister of Citizenship and Immigration), 2009 FCA 31, at para 7, stated that “[t]he examination of a claim under subsection 97(1) of the Act necessitates an individualized inquiry, which is to be conducted on the basis of the evidence adduced by a claimant ‘in the context of a present or prospective risk’ for him” [emphasis in original].
- Evidence: `governing_rule` cue `under` at chunk `5222746` offsets `249-254`; context: [30] The Court of Appeal in Sanchez v Canada (Minister of Citizenship and Immigration), 2007 FCA 99, at para 15, cited in Prophète v Canada (Minister of Citizenship and Immigration), 2009 FCA 31, at para 7, stated that “[t]he examination of a claim under subsection 97(1) of the Act necessitates an individualized inquiry, which is to be conducted on the basis of the evidence adduced by a claimant ‘in the context of a present or prospective risk’ for him” [emphasis in original].

#### 26003:1:subtheme:5 · paragraphs 31-34

- Raw key terms: `generally, risk, countries, criminal, example, faced, gang, protection`
- Display key terms: `generally, risk, countries, criminal, example, faced, gang, protection`
- Argument roles: `counterargument_limitation, governing_rule, issue`
- Explanation: Observed roles: counterargument_limitation, governing_rule, issue Display terms: generally, risk, countries, criminal, example, faced, gang, protection Rule/authority context: In most countries, and in most circumstances, persecution constituting a risk to life or rising to the level of cruel and unusual punishment, will also constitute criminal conduct under domestic criminal statutes. | [34] I do not accept that protection under the Act is limited in the manner submitted by the respondent. Evidence spans paragraphs 31-34. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5222747` offsets `371-379`; context: In examining the nature of the risk, the question is not whether the risk amounts to being a victim of crime.
- Evidence: `governing_rule` cue `under` at chunk `5222747` offsets `620-625`; context: In most countries, and in most circumstances, persecution constituting a risk to life or rising to the level of cruel and unusual punishment, will also constitute criminal conduct under domestic criminal statutes.
- Evidence: `governing_rule` cue `under` at chunk `5222750` offsets `37-42`; context: [34] I do not accept that protection under the Act is limited in the manner submitted by the respondent.
- Evidence: `counterargument_limitation` cue `However` at chunk `5222750` offsets `273-280`; context: However, where a person is specifically and personally targeted for death by a gang in circumstances where others are generally not, then he or she is entitled to protection under s.

#### 26003:1:subtheme:6 · paragraphs 35-36

- Raw key terms: `immigration, action, alberta, allowed, appeal, applicant, application, appropriate`
- Display key terms: `action, alberta, allowed, appropriate`
- Argument roles: `disposition, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: disposition, governing_rule, issue, reasoning_application Display terms: action, alberta, allowed, appropriate Rule/authority context: JUDGMENT THIS COURT’S JUDGMENT is that the application is allowed, the decision of the Board is set aside, the applicant’s claim for protection under s. Application context: In light of the disposition made of this application, the question the applicant proposes would not be dispositive of an appeal, and it is therefore not appropriate for certification. Operative outcome context: JUDGMENT THIS COURT’S JUDGMENT is that the application is allowed, the decision of the Board is set aside, the applicant’s claim for protection under s. Evidence spans paragraphs 35-36. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5222751` offsets `47-55`; context: [35] The applicant proposed that the following question be certified: “Can a risk which was initially random, indiscriminate, or general, be personalized through subsequent action of either the persecutor or victim, such as where there is an escalating or targeted reprisal for a refusal to pay?
- Evidence: `governing_rule` cue `under` at chunk `5222751` offsets `710-715`; context: JUDGMENT
THIS COURT’S JUDGMENT is that the application is allowed, the decision of the Board is set aside, the applicant’s claim for protection under s.
- Evidence: `reasoning_application` cue `therefore` at chunk `5222751` offsets `521-530`; context: In light of the disposition made of this application, the question the applicant proposes would not be dispositive of an appeal, and it is therefore not appropriate for certification.
- Evidence: `disposition` cue `allowed` at chunk `5222751` offsets `624-631`; context: JUDGMENT
THIS COURT’S JUDGMENT is that the application is allowed, the decision of the Board is set aside, the applicant’s claim for protection under s.

#### Section text

Guerrero v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2011-10-21
Neutral citation
2011 FC 1210
File numbers
IMM-2002-11
Notes
Reported Decision
Decision Content
Federal Court
Cour fédérale
Date: 20111021
Docket: IMM-2002-11
Citation: 2011 FC 1210
Ottawa, Ontario, October 21, 2011
PRESENT: The Honourable Mr. Justice Zinn
BETWEEN:
BENANCIO CORADO GUERRERO
Applicant
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
REASONS FOR JUDGMENT AND JUDGMENT

[1] Benancio Corado Guerrero is a citizen of Guatemala. He sought protection in Canada as a Convention refugee under s. 96 and as a person in need of protection under s. 97 of the Immigration and Refugee Protection Act, SC 2001, c 27. His claims were dismissed by the Refugee Protection Division of the Immigration and Refugee Board in its decision of February 28, 2011. The risk he alleged has no nexus to a Convention ground. In this application he challenged only the decision under s. 97 of the Act.

[2] The applicant submits that the Board (1) erred in misstating or misconstruing the nature of the risk he faced, thus rendering its analysis invalid, and (2) erred in determining that he did not face a personal risk pursuant to s. 97 of the Act.

[3] The issues in this case are questions of mixed fact and law are therefore reviewable under the standard of reasonableness: Dunsmuir v New Brunswick, 2008 SCC 9.

[4] This application must be allowed and the Board’s decision that the applicant was not a person in need of protection under s. 97 of the Act set aside. The Board reached its decision on erroneous findings of fact made in a perverse or capricious manner without regard for the material before it, as described in s. 18.1(4) of the Federal Courts Act, RSC 1985, c F-7. This error led the Board to unreasonably conclude that the risk faced by the applicant was one faced generally by others in Guatemala.

[5] The Board found the applicant to be credible; it believed what he said in support of his claim. Critically, the recitation of facts by the Board, in some instances, fails to include significant facts from the applicant’s evidence and, in other instances, includes alleged “facts” that are not supported by the record.

[6] The following summary of the key events is taken from the applicant’s amended Personal Information Form narrative (PIF), his oral testimony before the Board, and the Exhibits accepted by the Board. Where there are differences between the evidence before the Board, which it accepted as accurate, and the facts as recited by the Board in its decision, they are noted.

[7] In 2006, the applicant was a 17 year old boy living with his grandmother in the small town of El Coco, in Jalpatagua, Jutiapa, Guatemala. El Coco is very close to the border between Guatemala and El Salvador. The name of the village is written by the Board as El Choco. All of the official documents before it clearly state that it is El Coco. Nothing turns on this error.

[8] The applicant’s father is dead and although he has a mother and siblings living elsewhere in Guatemala, they are not in his life and have not been since his mother abandoned him when he was about eight years old. Effectively, his grandmother, with whom he lived, was his only family. In 2006, the applicant was in school and hoped to become a teacher.

[9] In August 2006, the applicant was walking with his friends Jorge and Byron past a small local casino. They were stopped by a man who told the friends to move aside as he wanted to talk with the applicant alone. In his PIF, the applicant states: “[H]e told me there was somebody who wanted me to work for them and I asked him how I could work for them and he told me that they needed someone to take some drugs from there to across the border to El Salvador.” The applicant responded that he would not do that because he was studying and he did not want to quit school. The man said that he would have to do it whether he wanted to or not. When the applicant repeated the conversation to his friends, they told him that “it was something that would happen to us sooner or later because these people were always trying to recruit young people to work for them.” He also told his grandmother who said they should pray that the men forget about him.

[10] The group that wanted him to transport drugs across the border is known as Los Lorenzanas.

[11] About three weeks after this initial encounter, the leader of Los Lorenzanas, together with about eight others, including the man who had previously spoken to the applicant, were waiting for him after school. He was directed to get into an SUV because someone wanted to talk to him. The leader of Los Lorenzanas told him that he was to take drugs into El Salvador. The applicant again said that he did not want to do that. He was then driven to his grandmother’s house where he was told by the leader that “the next time was not going to be like this” and that he or his grandmother would pay with their lives. The applicant again told his grandmother of this encounter and she said not to worry because “their threat wouldn’t become true.”

[12] Nothing further happened until the evening of October 2, 2006. The applicant testified that he was getting ready to eat supper with his grandmother when he heard a vehicle stop in front of the house. He went to the window and saw two men in a truck draw automatic weapons. “[T]hey rolled down the windows and they started to shoot with the rifles against her -- at her.” In his PIF he wrote that they “started firing at the house.” He continued his testimony saying that “I was able to throw myself on the ground and when I rolled to her she was dead under the table and I ran away.” Although a careful review of the certified tribunal record suggests some contradictions concerning the details of this engagement, it is uncontested that his grandmother was shot multiple times. The death certificate shows that she died on October 2, 2006 as a “consequence of Various bullet impacts in different parts of the body, unknown calibre” [emphasis in original]. The translated police report reveals the ferocity of the attack. It describes the bullet wounds the grandmother suffered:
2 wounds in the chest, 1 wound in the wall of right axillaries, 2 wounds in the right side, 2 wounds in the cheek and mouth on the left side, 1 wound in the head region, 2 wounds on the back left side and 1 wound on the little finger of the left hand, caused by unknown individuals who fled after the fact to unknown direction.

[13] The Board, at paragraph 24 of its decision, writes of this event and states that “[w]hen the organization persisted in recruiting the claimant and he continued to refuse their offers of money, membership, and a gun to carry, they became angry and retaliated by threatening and then shooting his grandmother in front of him to make their point.” Notwithstanding the Board’s colourful description of the recruiting tactics of Los Lorenzanas, there is nothing in the record to support its statement that the applicant was offered money, membership or guns. To the contrary, the Board specifically asked the applicant if he was asked to join their group and he responded: “They didn’t ask me but if I do something for them it’s as though I already belonged to them.”

[14] By erroneously stating that the group was attempting to recruit the applicant to join it through promises of guns, membership and money, the Board completely mischaracterized the interaction between the applicant and Los Lorenzanas. The evidence before the Board was that Los Lorenzanas specifically targeted the applicant to work for them to carry drugs across the border, not merely to join their organization, as the Board states.

[15] Further, although the Board at paragraph 24 finds that the grandmother’s shooting was in retaliation for the applicant refusing the recruitment by Los Lorenzanas, at paragraph 28 of its decision, the Board writes: “I find that the grandmother was harmed incidentally and not as a means to recruit the claimant” [emphasis added]. The Board’s characterization of the violent death of the grandmother from multiple gun shots as having been “harmed” is a perverse mischaracterization. She was killed.

[16] Also perverse is the Board’s finding that her death was “incidental” when the testimony of the applicant, supported by the evidence of the police report and the previous threats, was that they shot at her. As is noted above, the applicant in his PIF did state that the killers “started firing at the house” but this must be considered in the context of all the evidence. This includes the fact that there is nothing in the police report or in the record that reveals that there were any bullet holes in the walls of the house. Given the 11 bullet wounds in the grandmother’s body, it is unreasonable to conclude that the grandmother’s wounds were “incidental.” In my view, the only reasonable view of the evidence is that the wounds were inflicted deliberately. She was targeted by these killers.

[17] Following the shooting, the applicant ran to his friend’s house where he was given enough money to travel to Guatemala City. Approximately seven months later he was in the marketplace in Guatemala City where he was approached by one of the men who had previously threatened him and his grandmother. He was again told to transport drugs across the border and told that this was the last time he would be asked; the next time he would be killed. The applicant asked for four days to return to El Coco and implied that he would do as they asked. Instead of returning, he left Guatemala.

[18] He traveled by foot and rail from Guatemala through Mexico and the United States of America before entering Canada at Vancouver on February 14, 2008. He filed a claim for protection in Calgary on July 9, 2008.

[19] In its appreciation of the evidence, the Board also considered a letter the applicant received from his two friends, Jorge and Byron, with whom he was walking when he was initially approached by a member of Los Lorenzanas, and with whom he had stayed in contact. In this letter, his friends confirm that the group that tried to get the applicant to transport drugs is Los Lorenzanas. The Board at paragraph 27 of its decision writes:
In their letter the friends inform the claimant that they have learned that the organization that operated in their home-village of El Choco [sic] is known as Los Lorenzanas; that they are a large organization with connections throughout Guatemala and neighboring countries and go by different names in different locations. They are the ‘mastermind’ organization and routinely hire the Mara 18 street gang to do their dirty work. It was the Maras 18 who were responsible for the murder of the claimant’s grandmother and for tracking the claimant down in Guatemala City.

[20] The Board is in error in its description of the content of the friends’ letter which can be found on page 293 of the certified tribunal record. It makes no reference at all to Los Lorenzanas being a “large organization” or to having “connections throughout Guatemala and neighboring countries” or to going “by different names in different locations.” In fact, other than this letter and the evidence of the applicant, there is nothing in the record that references Los Lorenzanas or describes the characteristics of the group. The applicant’s friends do however write that they believe that Los Lorenzanas hired Mara 18 to find and kill him. This supports the evidence of the applicant at page 324 of the certified tribunal record that Los Lorenzanas hired Mara 18 to look for and to “assassinate” him.

[21] The Board found that the harm the applicant feared was “criminality (recruitment to deliver drugs)” and that this was not linked to a Convention ground in s. 96 of the Act. While I agree that s. 96 was not at play, the Board’s conclusion as to the harm the applicant feared is perverse. It is clear from the evidence before the Board that the applicant did not base his claim on a fear of recruitment. Further, if there was recruitment, it was not to join Los Lorenzanas but to transport drugs for them. He had already said no to that demand. His fear was a fear of death by a third party organization – the Mara 18. This third party organization, as stated earlier, had been hired by Los Lorenzanas to kill the applicant.

[22] The Board analysed its view of the applicant’s risk under s. 97 of the Act. The Board acknowledged the general violence that is prevalent in Guatemala and noted that it is primarily drug related. The Board then noted that the applicant was a prime target for recruitment because of his vulnerable age and social profile. It was noted that he was young, naïve, unsophisticated and uneducated. It was also noted that he was orphaned and had lived with his elderly grandmother since he was eight years old, without a family and strong social support to help him make crucial decisions in life. The Board stated that he was a particular target because of his geographic location of being so close to the El Salvador border. The Board also noted that what made the applicant “a particular target of the drug trafficking gang was his refusal to deliver drugs to the border of El Salvador.” Notwithstanding its finding that the applicant was targeted, the Board found that the risk he faced was a generalized one, given the pervasiveness of gangs in Guatemala.

[23] In my view, the errors outlined above resulted in the Board mischaracterizing the personal circumstances of the applicant and thus led the Board to inaccurately find that his circumstances and his risk of harm was one faced generally by others. He was not, like many his age, merely at risk of recruitment by a criminal gang. Rather, he was at risk of death having been specifically and personally targeted by a criminal organization for death at the hand of Mara 18 who had been hired to kill him.

[24] This finding is dispositive of the application for judicial review; the decision under review is unreasonable and the applicant’s claim for protection must be redetermined. Nevertheless, I wish to add a few comments concerning s. 97 of the Act and, in particular, the respondent’s interpretation of the recent decision in Baires Sanchez v Canada (Minister of Citizenship and Immigration), 2011 FC 993 [Baires Sanchez], which he submitted is dispositive of the present application.

[25] Subparagraph 97(1)(b)(ii) of the Act defines a person in need of protection as “a person in Canada whose removal to their country or countries of nationality … would subject them personally to a risk to their life or a risk of cruel and unusual treatment or punishment if the risk would be faced by the person in every part of that country and is not faced generally by other individuals in or from that country.”

[26] Parsing this provision, it is evident that if a claimant is to be found to be a person in need of protection, then it must be found that:
a. The claimant is in Canada;
b. The claimant would be personally subjected to a risk to their life or to cruel and unusual treatment or punishment if returned to their country of nationality;
c. The claimant would face that personal risk in every part of their country; and
d. The personal risk the claimant faces “is not faced generally by other individuals in or from that country.”
All four of these elements must be found if the person is to meet the statutory definition of a person in need of protection; it is only such persons who are permitted to remain in Canada.

[27] The majority of cases turn on whether or not the last condition has been satisfied, that is, whether the risk faced by the claimant is a risk faced generally by others in the country. I pause to observe that regrettably too many decisions of the RPD and of this Court use imprecise language in this regard. No doubt I too have been guilty of this. Specifically, many decisions state or imply that a generalized risk is not a personal risk. What is usually meant is that the claimant’s risk is one faced generally by others and thus the claimant does not meet the requirements of the Act. It is not meant that the claimant has no personal risk. It is important that a decision-maker finds that a claimant has a personal risk because if there is no personal risk to the claimant, then there is no need to do any further analysis of the claim; there is simply no risk. It is only after finding that there is a personal risk that a decision-maker must continue to consider whether that risk is one faced generally by the population.

[28] My second observation is that too many decision-makers inaccurately describe the risk the applicant faces and too many decision-makers fail to actually state the risk altogether.
Paragraph 97(1)(b) of the Act is quite specific: The personal risk a claimant must face is “a risk to their life or to a risk of cruel and unusual treatment or punishment.” Before determining whether the risk faced by the claimant is one generally faced by others in the country, the decision-maker must (1) make an express determination of what the claimant’s risk is, (2) determine whether that risk is a risk to life or a risk of cruel and unusual treatment or punishment, and (3) clearly
express the basis for that risk.

[29] An example of the sort of decision I am addressing is that under review. The closest the decision-maker in this case comes to actually stating the risk she finds this applicant faces is the following: “[T]he harm feared by the claimant; that is criminality (recruitment to deliver drugs)….” But this is not the risk faced by the applicant, and even if it were, the decision fails to state how this meets the test of risk set out in subparagraph 97(1)(b)(ii) of the Act. At best, the risk as described forms part of the reason for the risk to the applicant’s life. When one conflates the reason for the risk with the risk itself, one fails to properly conduct the individualized inquiry of the claim that is essential to a proper s. 97 analysis and determination.

[30] The Court of Appeal in Sanchez v Canada (Minister of Citizenship and Immigration), 2007 FCA 99, at para 15, cited in Prophète v Canada (Minister of Citizenship and Immigration), 2009 FCA 31, at para 7, stated that “[t]he examination of a claim under subsection 97(1) of the Act necessitates an individualized inquiry, which is to be conducted on the basis of the evidence adduced by a claimant ‘in the context of a present or prospective risk’ for him” [emphasis in original]. The words “in the context of” in this statement are of fundamental importance. The decision-maker must examine the claimant’s evidence and the claimant’s circumstances in the context of the risk to him.

[31] In Mendoza v Canada (Minister of Citizenship and Immigration), 2010 FC 648, at paras 35- 36, I attempted to flesh out what such an individualized inquiry entails. I wrote that:
In conducting the individualized inquiry the Board must examine both the nature of the risk faced by claimants as well as the agent of persecution. In examining the nature of the risk, the question is not whether the risk amounts to being a victim of crime. In most countries, and in most circumstances, persecution constituting a risk to life or rising to the level of cruel and unusual punishment, will also constitute criminal conduct under domestic criminal statutes. The question is not whether all citizens in a country face a possibility of being a victim of such crimes. We all face the possibility of being the victim of a crime each and every day.
The relevant question is whether the risk is one generally faced by all citizens. Generally, in this sense, is to be given its ordinary meaning. What is general in one country may not be general in another country. In Canada, we generally face a risk of being involved in a motor vehicle accident each time we drive, even though the p

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]


## 26003:2 · paragraphs 37-37

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `f53c4df95c07feb59c00475b40b196fdf76c18783a0030594ca254455cb4dd5d`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 26003:2:subtheme:1 · paragraphs 37-37

- Raw key terms: `alberta, appearances, applicant, attorney, barristers, bjorn, calgary, canada`
- Display key terms: `alberta, barristers, bjorn, calgary`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: alberta, barristers, bjorn, calgary No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 37-37. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT
AND JUDGMENT: ZINN J.
DATED: October 21, 2011
APPEARANCES:
Bjorn Harsanyi
FOR THE APPLICANT
Rick Garvin
FOR THE RESPONDENT
SOLICITORS OF RECORD:
STEWART SHARMA HARSANYI
Barristers and Solicitors
Calgary, Alberta
FOR THE APPLICANT
MYLES J. KIRVAN
Deputy Attorney General of Canada
Calgary, Alberta
FOR THE RESPONDENT
