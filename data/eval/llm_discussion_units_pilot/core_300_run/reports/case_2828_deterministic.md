# Discussion Units: case 2828

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **19**
- Continuity pairs: **18**
- Discussion Units: **2**
- Paragraph source hashes: **19**
- Sub-themes: **6**

## 2828:1 · paragraphs 0-17

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `7c2fe44810cb5172db124e8b14df9184a3fd18d6e61ec3aa39c501f527764da8`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 2828:1:subtheme:1 · paragraphs 0-4

- Raw key terms: `applicant, costa, rica, assistance, children, decision, immigration, protection`
- Display key terms: `costa, rica, assistance, children, protection`
- Argument roles: `disposition, party_position`
- Explanation: Observed roles: disposition, party_position Display terms: costa, rica, assistance, children, protection Position/evidence statements: She claimed to have a well-founded fear of her former common law spouse who allegedly abused her and her children. Operative outcome context: [1] The Applicant (and her minor children) had their claim for refugee status / person in need of protection status dismissed by the Refugee Protection Division ("RPD") of the Immigration and Refugee Board. Evidence spans paragraphs 0-4. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `disposition` cue `dismissed` at chunk `4196088` offsets `116-125`; context: [1] The Applicant (and her minor children) had their claim for refugee status / person in need of protection status dismissed by the Refugee Protection Division ("RPD") of the Immigration and Refugee Board.
- Evidence: `party_position` cue `claimed` at chunk `4196089` offsets `57-64`; context: She claimed to have a well-founded fear of her former common law spouse who allegedly abused her and her children.

#### 2828:1:subtheme:2 · paragraphs 5-7

- Raw key terms: `protection, state, adequacy, applicant, case, costa, crucial, deal`
- Display key terms: `protection, state, adequacy, case, costa, crucial, deal`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: protection, state, adequacy, case, costa, crucial, deal Rule/authority context: [6] Both parties agree that the standard of review applicable to a determination of the adequacy of state protection is patent unreasonableness. Application context: )(QL) where the Board was required to assess credibility as part of its analysis and was therefore owed a high level of deference, in this instance the RPD was not required to deal with credibility. Evidence spans paragraphs 5-7. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4196092` offsets `18-24`; context: [5] The principal issues raised by the Applicant are (1) whether the RPD failed to consider evidence contrary to the conclusion that Costa Rica provided adequate state protection for abused women; (2) whether the RPD was required to explicitly state its reasons for preferring some evidence over other contrary evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `4196092` offsets `92-100`; context: [5] The principal issues raised by the Applicant are (1) whether the RPD failed to consider evidence contrary to the conclusion that Costa Rica provided adequate state protection for abused women; (2) whether the RPD was required to explicitly state its reasons for preferring some evidence over other contrary evidence.
- Evidence: `governing_rule` cue `standard of review` at chunk `4196093` offsets `32-50`; context: [6] Both parties agree that the standard of review applicable to a determination of the adequacy of state protection is patent unreasonableness.
- Evidence: `reasoning_application` cue `therefore` at chunk `4196093` offsets `485-494`; context: )(QL) where the Board was required to assess credibility as part of its analysis and was therefore owed a high level of deference, in this instance the RPD was not required to deal with credibility.
- Evidence: `evidence_fact` cue `evidence` at chunk `4196094` offsets `374-382`; context: This purely subjective view of the adequacy of Costa Rica state protection is not "direct, relevant and compelling" evidence of the inadequacy of state protection.

#### 2828:1:subtheme:3 · paragraphs 8-11

- Raw key terms: `applicant, evidence, applicant's, cannot, case, costa, efforts, ignored`
- Display key terms: `applicant's, cannot, case, costa, efforts, ignored`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position Display terms: applicant's, cannot, case, costa, efforts, ignored Position/evidence statements: [10] The Applicant further argues that the RPD ignored evidence submitted by her tending to show that Costa Rica had difficulty protecting abused women. | Not only is there a presumption that a tribunal has considered material submitted to it, in this case, at p. Evidence spans paragraphs 8-11. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4196095` offsets `223-231`; context: )(QL) imposed a greater obligation to seek assistance where there is a developed democracy:
When the state in question is a democratic state, as in the case at bar, the claimant must do more than simply show that he or she went to see some members of the police force and that his or her efforts were unsuccessful.
- Evidence: `evidence_fact` cue `evidence` at chunk `4196096` offsets `192-200`; context: Whatever the depth of the Applicant's belief, she must do more than she did given the evidence of the nature of the political, judicial and administrative structure of Costa Rica.
- Evidence: `party_position` cue `argues` at chunk `4196097` offsets `27-33`; context: [10] The Applicant further argues that the RPD ignored evidence submitted by her tending to show that Costa Rica had difficulty protecting abused women.
- Evidence: `evidence_fact` cue `evidence` at chunk `4196097` offsets `55-63`; context: [10] The Applicant further argues that the RPD ignored evidence submitted by her tending to show that Costa Rica had difficulty protecting abused women.
- Evidence: `party_position` cue `submitted` at chunk `4196098` offsets `202-211`; context: Not only is there a presumption that a tribunal has considered material submitted to it, in this case, at p.
- Evidence: `evidence_fact` cue `evidence` at chunk `4196098` offsets `71-79`; context: [11] Despite counsel's best efforts, the fact remains that there is no evidence that the RPD ignored this contradictory evidence.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `4196098` offsets `333-339`; context: It cannot be assumed that if the RPD referred to some of this evidence, it must have ignored the rest.

#### 2828:1:subtheme:4 · paragraphs 12-15

- Raw key terms: `case, certain, evidence, preference, applicant's, decision, documentary, documents`
- Display key terms: `case, certain, preference, applicant's, documentary, documents`
- Argument roles: `evidence_fact, governing_rule, issue, party_position`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, party_position Display terms: case, certain, preference, applicant's, documentary, documents Position/evidence statements: [12] Finally the Applicant argues that the RPD failed to explain why it preferred some documentary evidence over other contrary evidence. Rule/authority context: The failure to explain may affect the degree of deference owed and the ability of a court to determine whether the tribunal has met the standard of review to which its decision maybe subject. Evidence spans paragraphs 12-15. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4196099` offsets `468-475`; context: The failure to explain may affect the degree of deference owed and the ability of a court to determine whether the tribunal has met the standard of review to which its decision maybe subject.
- Evidence: `party_position` cue `argues` at chunk `4196099` offsets `27-33`; context: [12] Finally the Applicant argues that the RPD failed to explain why it preferred some documentary evidence over other contrary evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `4196099` offsets `99-107`; context: [12] Finally the Applicant argues that the RPD failed to explain why it preferred some documentary evidence over other contrary evidence.
- Evidence: `governing_rule` cue `standard of review` at chunk `4196099` offsets `501-519`; context: The failure to explain may affect the degree of deference owed and the ability of a court to determine whether the tribunal has met the standard of review to which its decision maybe subject.
- Evidence: `evidence_fact` cue `evidence` at chunk `4196100` offsets `253-261`; context: The RPD's preference for other documents can be garnered from a reading of the decision as a whole - it turns on the weight of the preferred evidence, its objectivity and its currency.
- Evidence: `evidence_fact` cue `evidence` at chunk `4196101` offsets `136-144`; context: [14] In this case as well, the reason for rejecting the Applicant's claim did not rest solely on the preference for certain documentary evidence.

#### 2828:1:subtheme:5 · paragraphs 16-17

- Raw key terms: `application, cause, certified, considering, counsel, court, date, decision`
- Display key terms: `certified, considering, date`
- Argument roles: `disposition, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, issue, reasoning_application Display terms: certified, considering, date Application context: Therefore this application will be dismissed. Operative outcome context: Therefore this application will be dismissed. Evidence spans paragraphs 16-17. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4196103` offsets `149-157`; context: No question will be certified.
- Evidence: `evidence_fact` cue `RECORD` at chunk `4196103` offsets `232-238`; context: JUDGE
FEDERAL COURT
NAMES OF COUNSEL AND SOLICITORS OF RECORD
DOCKET: IMM-7329-04
- Evidence: `reasoning_application` cue `Therefore` at chunk `4196103` offsets `100-109`; context: Therefore this application will be dismissed.
- Evidence: `disposition` cue `dismissed` at chunk `4196103` offsets `135-144`; context: Therefore this application will be dismissed.

#### Section text

Martinez v. Canada (Minister of Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2005-07-29
Neutral citation
2005 FC 1050
File numbers
IMM-7329-04
Decision Content
Docket: IMM-7329-04
Citation: 2005 FC 1050
OTTAWA, Ontario, July 29, 2005
BETWEEN:
Dunnia Patricia Suarez Martinez, Daniela Suarez Martinez
and Keylor Antonio Suarez Martinez
Applicants
and
The Minister of Citizenship and Immigration
Respondents
REASONS FOR ORDER
PHELAN J.

[1] The Applicant (and her minor children) had their claim for refugee status / person in need of protection status dismissed by the Refugee Protection Division ("RPD") of the Immigration and Refugee Board. The claim was rejected on the basis of the failure to rebut the presumption of state protection in Costa Rica. This is the judicial review of the RPD's decision.
Background

[2] The Applicant is a female citizen of Costa Rica. She claimed to have a well-founded fear of her former common law spouse who allegedly abused her and her children.

[3] In November 1998 the Applicant reported her spouse's abuse to the local police. She received no assistance. In December 1998 she attempted to report her spouse to police in a different town. She was advised that they had no jurisdiction in her hometown and that she had to make her report to the local police. She took no further action other than to leave Costa Rica in August 2000.

[4] The RPD held that in a democracy such as Costa Rica, the Applicant must do more than what she did to seek protection, as these were other courses open to her. Her explanation for not seeking assistance from other sources is that she did not believe that she would be protected.

[5] The principal issues raised by the Applicant are (1) whether the RPD failed to consider evidence contrary to the conclusion that Costa Rica provided adequate state protection for abused women; (2) whether the RPD was required to explicitly state its reasons for preferring some evidence over other contrary evidence.
Determination

[6] Both parties agree that the standard of review applicable to a determination of the adequacy of state protection is patent unreasonableness. The Court has considered this aspect of the decision on the basis of both patent unreasonableness and reasonableness simpliciter. Unlike my decision in Malik v. Canada (Minister of Citizenship and Immigration), 2004 FC 189, [2004] F.C.J. No. 217 (F.C.)(QL) where the Board was required to assess credibility as part of its analysis and was therefore owed a high level of deference, in this instance the RPD was not required to deal with credibility. In any event, the standard of review is not a crucial matter of distinction in this case.

[7] What is crucial to this case is that the Applicant made only two attempts to seek assistance, one of which was to police who had no local jurisdiction to deal with her complaint. She then formed the opinion that no other assistance would be forthcoming. This purely subjective view of the adequacy of Costa Rica state protection is not "direct, relevant and compelling" evidence of the inadequacy of state protection.

[8] The Court of Appeal in N.K. v. Canada (Minister of Citizenship and Immigration), [1996] F.C.J. no. 1376 (C.A.)(QL) imposed a greater obligation to seek assistance where there is a developed democracy:
When the state in question is a democratic state, as in the case at bar, the claimant must do more than simply show that he or she went to see some members of the police force and that his or her efforts were unsuccessful. The burden of proof that rests on the claimant is, in a way, directly proportional to the level of democracy in the state in question: the more democratic the state's institutions, the more the claimant must have done to exhaust all the courses of action open to him or her.

[9] The determination of adequacy of state protection cannot rest on the subjective fear of an applicant. Whatever the depth of the Applicant's belief, she must do more than she did given the evidence of the nature of the political, judicial and administrative structure of Costa Rica. The RPD's conclusion that the Applicant had "to do more" is itself more than reasonable.

[10] The Applicant further argues that the RPD ignored evidence submitted by her tending to show that Costa Rica had difficulty protecting abused women. That evidence included a variety of items such as newspaper articles, an e-mail "blog" and a report by a human rights organization on the application of the Convention on Rights of the Child by Costa Rica.

[11] Despite counsel's best efforts, the fact remains that there is no evidence that the RPD ignored this contradictory evidence. Not only is there a presumption that a tribunal has considered material submitted to it, in this case, at p. 2 of the decision, there is reference to some of the documents submitted by the Applicant. It cannot be assumed that if the RPD referred to some of this evidence, it must have ignored the rest. Quite the opposite assumption could be made. There simply is no evidence to support the Applicant's contention that the submitted documents were ignored.

[12] Finally the Applicant argues that the RPD failed to explain why it preferred some documentary evidence over other contrary evidence. There is no absolute requirement for such an explanation. The circumstances of the case dictate the nature and extent of the duty to give reasons, of which the explanation of the preference for certain evidence is a component. The failure to explain may affect the degree of deference owed and the ability of a court to determine whether the tribunal has met the standard of review to which its decision maybe subject.

[13] In this case, the Applicant's documents are not so compelling as to call for an explanation for rejection. The RPD's preference for other documents can be garnered from a reading of the decision as a whole - it turns on the weight of the preferred evidence, its objectivity and its currency.

[14] In this case as well, the reason for rejecting the Applicant's claim did not rest solely on the preference for certain documentary evidence. It also turned on the Applicant's evidence and her efforts to seek protection.

[15] In my view there are sufficient reasons given which explain the RPD's conclusion. While in many cases further and explicit explanations for favouring certain documents may not only be preferable but required, such is not the case here.

[16] Finally, considering the decision as a whole, I can find no reason for the Court to intervene. Therefore this application will be dismissed. No question will be certified.
JUDGE
FEDERAL COURT
NAMES OF COUNSEL AND SOLICITORS OF RECORD
DOCKET: IMM-7329-04

STYLE OF CAUSE: DUNNIA PATRICIA SUAREZ MARTINEZ ET AL v. MCI
PLACE OF HEARING: Toronto, Ontario
DATE OF HEARING: July 14, 2005
REASONS FOR 

## 2828:2 · paragraphs 18-18

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `5c199a9aca484b6ccae261430746dfc756a6c0e43bc27c7d966e33e995b71ca3`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 2828:2:subtheme:1 · paragraphs 18-18

- Raw key terms: `ahunwan, appearances, applicants, boniface, bonifsce, brad, dated, gotkin`
- Display key terms: `ahunwan, boniface, bonifsce, brad, dated, gotkin`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: ahunwan, boniface, bonifsce, brad, dated, gotkin No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 18-18. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

ORDER : Phelan J.
DATED: July 29, 2005
APPEARANCES:
Boniface Ahunwan FOR APPLICANTS
Toronto, Ontario
Brad Gotkin FOR RESPONDENT
Toronto, Ontario
SOLICITORS OF RECORD:
Bonifsce Ahunwan FOR APPLICANTS
Toronto, Ontario
Brad Gotkin FOR RESPONDENT
Toronto Ontario
