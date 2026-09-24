# Discussion Units: case 11430

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **37**
- Continuity pairs: **36**
- Discussion Units: **4**
- Paragraph source hashes: **37**
- Sub-themes: **13**

## 11430:1 · paragraphs 0-3

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `a33b84f4988b66e5395f820e51377bce1e15c23f841c6ce8716217b57d63ac6a`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 11430:1:subtheme:1 · paragraphs 0-3

- Raw key terms: `applicant, appeal, applicants, bisexual, children, conclusions, court, decision`
- Display key terms: `bisexual, children, conclusions`
- Argument roles: `evidence_fact`
- Explanation: Observed roles: evidence_fact Display terms: bisexual, children, conclusions Evidence spans paragraphs 0-3. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `testimony` at chunk `4575725` offsets `86-95`; context: [2] The RPD found the Applicant to lack credibility, largely on the basis of her oral testimony, and concluded that the Applicant is not a bisexual woman and thus does not have a fear of persecution on a balance of probabilities.
- Evidence: `evidence_fact` cue `evidence` at chunk `4575726` offsets `114-122`; context: [3] On appeal to this Court, the Applicant advances two arguments: the RAD drew unreasonable conclusions from the evidence, and the RAD erred in its assessment of the documentary evidence.

#### Section text

Oranye v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2018-04-11
Neutral citation
2018 FC 390
File numbers
IMM-3178-17
Decision Content
Date: 20180411
Docket: IMM-3178-17
Citation: 2018 FC 390
Ottawa, Ontario, April 11, 2018
PRESENT: The Honourable Mr. Justice Ahmed
BETWEEN:
ONAJITE ROSEMARY ORANYE
JOSHUA IKECHUKWU ORANYE (MINOR)
JORDAN OBINNA ORANYE (MINOR)
JASMIN ADAEZE ORANYE (MINOR)
Applicants
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
JUDGMENT AND REASONS
I. Overview

[1] This case concerns a decision of the Refugee Appeal Division (RAD) upholding a decision of the Refugee Protection Division (RPD) to reject the Applicants’ claim for protection as Convention refugees or persons in need of protection. The principal Applicant is a 41 year old citizen of Nigeria, who claims a fear of persecution on behalf of herself and her three minor children. As a bisexual woman, she claims that she and her children may be subjected to “ritual cleansings” and female genital mutilation should they return to Nigeria, now that her sexual orientation is known to the police, her community, and her husband’s family.

[2] The RPD found the Applicant to lack credibility, largely on the basis of her oral testimony, and concluded that the Applicant is not a bisexual woman and thus does not have a fear of persecution on a balance of probabilities. The Applicant’s documentary evidence was also given diminished weight. The RAD, for its part, largely relied upon the credibility findings of the RPD as it found them to be reasonable. In its independent analysis, the RAD reviewed the Applicant’s documentary evidence, again confirming the conclusions of the RPD. It then proceeded to further analyze the Nigeria country condition documents and found that the Applicant and her children are unlikely to be subjected to female genital mutilation and other cleansing rituals should they return to Nigeria.

[3] On appeal to this Court, the Applicant advances two arguments: the RAD drew unreasonable conclusions from the evidence, and the RAD erred in its assessment of the documentary evidence.


## 11430:2 · paragraphs 4-16

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `fcaf9a69cb0f292a70764ce454e81a33663972a6ba87035ddab8d6d9b7d07732`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 11430:2:subtheme:1 · paragraphs 4-10

- Raw key terms: `applicant, children, family, jimmy, nigeria, nigerian, police, august`
- Display key terms: `children, family, jimmy, nigeria, nigerian, police, august`
- Argument roles: `counterargument_limitation, disposition, governing_rule, party_position`
- Explanation: Observed roles: counterargument_limitation, disposition, governing_rule, party_position Display terms: children, family, jimmy, nigeria, nigerian, police, august Position/evidence statements: [5] The Applicant asserts that she is a bisexual woman. Rule/authority context: Jimmy nevertheless continued to pursue the Applicant, and, under pressure from her family, she married him in April 2009. | Decision Under Review Operative outcome context: [8] The Applicant’s claim for protection was heard by the RPD but was denied on the grounds that the member did not find the Applicant to be credible on the core elements of her claim: notably that she is a bisexual woma | In a decision (“the RAD Decision”) dated June 26, 2017, the RAD upheld the RPD decision to reject the Applicant’s claim for protection. Evidence spans paragraphs 4-10. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `party_position` cue `asserts` at chunk `4575728` offsets `18-25`; context: [5] The Applicant asserts that she is a bisexual woman.
- Evidence: `governing_rule` cue `under` at chunk `4575728` offsets `676-681`; context: Jimmy nevertheless continued to pursue the Applicant, and, under pressure from her family, she married him in April 2009.
- Evidence: `counterargument_limitation` cue `nevertheless` at chunk `4575728` offsets `623-635`; context: Jimmy nevertheless continued to pursue the Applicant, and, under pressure from her family, she married him in April 2009.
- Evidence: `counterargument_limitation` cue `but` at chunk `4575731` offsets `62-65`; context: [8] The Applicant’s claim for protection was heard by the RPD but was denied on the grounds that the member did not find the Applicant to be credible on the core elements of her claim: notably that she is a bisexual woman and fears that she and her children could be persecuted by her husband’s family and the Nigerian police should she return.
- Evidence: `disposition` cue `denied` at chunk `4575731` offsets `70-76`; context: [8] The Applicant’s claim for protection was heard by the RPD but was denied on the grounds that the member did not find the Applicant to be credible on the core elements of her claim: notably that she is a bisexual woman and fears that she and her children could be persecuted by her husband’s family and the Nigerian police should she return.
- Evidence: `governing_rule` cue `Under` at chunk `4575732` offsets `263-268`; context: Decision Under Review
- Evidence: `disposition` cue `upheld` at chunk `4575732` offsets `103-109`; context: In a decision (“the RAD Decision”) dated June 26, 2017, the RAD upheld the RPD decision to reject the Applicant’s claim for protection.

#### 11430:2:subtheme:2 · paragraphs 11-12

- Raw key terms: `affirms, applicant, because, decision, documentary, evidence, finds, para`
- Display key terms: `affirms, because, documentary, finds, para`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: affirms, because, documentary, finds, para Rule/authority context: First, the RAD reviews the RPD’s findings with respect to the Applicant’s sexual orientation, documentary evidence, and analysis under s. Application context: The RAD finds that the Applicant was not credible because of perceived hesitations, because the Applicant was unable to explain how she juggled two relationships at the same time, because the Applicant was inconsistent a | [11] With respect to the documentary evidence, the RAD finds that the RPD approach was reasonable; notably, photographs were given little weight for lack of identifying dates or features, affidavits and other documentary Evidence spans paragraphs 11-12. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4575733` offsets `583-590`; context: The RAD finds that the Applicant was not credible because of perceived hesitations, because the Applicant was unable to explain how she juggled two relationships at the same time, because the Applicant was inconsistent about whether her sexual relationship with “A.
- Evidence: `evidence_fact` cue `evidence` at chunk `4575733` offsets `155-163`; context: First, the RAD reviews the RPD’s findings with respect to the Applicant’s sexual orientation, documentary evidence, and analysis under s.
- Evidence: `governing_rule` cue `under` at chunk `4575733` offsets `178-183`; context: First, the RAD reviews the RPD’s findings with respect to the Applicant’s sexual orientation, documentary evidence, and analysis under s.
- Evidence: `reasoning_application` cue `because` at chunk `4575733` offsets `408-415`; context: The RAD finds that the Applicant was not credible because of perceived hesitations, because the Applicant was unable to explain how she juggled two relationships at the same time, because the Applicant was inconsistent about whether her sexual relationship with “A.
- Evidence: `evidence_fact` cue `evidence` at chunk `4575734` offsets `37-45`; context: [11] With respect to the documentary evidence, the RAD finds that the RPD approach was reasonable; notably, photographs were given little weight for lack of identifying dates or features, affidavits and other documentary evidence from Nigeria were given diminished probative value due to a lack of envelopes and spelling/typographical errors, and letters provided by Canadian LGBTQ support organizations were given diminished weight because they do not “confer sexual identity” (RAD Decision, para.
- Evidence: `reasoning_application` cue `because` at chunk `4575734` offsets `433-440`; context: [11] With respect to the documentary evidence, the RAD finds that the RPD approach was reasonable; notably, photographs were given little weight for lack of identifying dates or features, affidavits and other documentary evidence from Nigeria were given diminished probative value due to a lack of envelopes and spelling/typographical errors, and letters provided by Canadian LGBTQ support organizations were given diminished weight because they do not “confer sexual identity” (RAD Decision, para.

#### 11430:2:subtheme:3 · paragraphs 13-14

- Raw key terms: `applicant, decision, further, need, para, analysis, argument, attendance`
- Display key terms: `further, need, para, analysis, argument, attendance`
- Argument roles: `evidence_fact, governing_rule, issue`
- Explanation: Observed roles: evidence_fact, governing_rule, issue Display terms: further, need, para, analysis, argument, attendance Rule/authority context: 97 analysis, finding that the RPD’s conclusion that the Applicant is not a bisexual woman meant that no further analysis under s. Evidence spans paragraphs 13-14. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4575735` offsets `262-269`; context: 97 was necessary to determine whether the Applicant is a person in need of protection (RAD Decision, para.
- Evidence: `governing_rule` cue `under` at chunk `4575735` offsets `223-228`; context: 97 analysis, finding that the RPD’s conclusion that the Applicant is not a bisexual woman meant that no further analysis under s.
- Evidence: `evidence_fact` cue `evidence` at chunk `4575736` offsets `75-83`; context: [13] The second part of the RAD Decision is the “independent review of the evidence,” which focuses exclusively on the documentary evidence.

#### 11430:2:subtheme:4 · paragraphs 15-16

- Raw key terms: `applicant, issues, affidavits, affirms, against, allocation, appeal, appropriate`
- Display key terms: `issues, affidavits, affirms, against, allocation, appropriate`
- Argument roles: `evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, party_position, reasoning_application Display terms: issues, affidavits, affirms, against, allocation, appropriate Position/evidence statements: On this basis, the RAD asserts that an allocation of low probative value is appropriate (RAD Decision, para. Application context: The RAD member further relies upon the NDP to conclude that, because the Applicant and her husband are against the practice of female genital mutilation, it is unlikely that the Applicant or her daughter will suffer this Evidence spans paragraphs 15-16. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Issues` at chunk `4575737` offsets `681-687`; context: Issues
- Evidence: `party_position` cue `asserts` at chunk `4575737` offsets `329-336`; context: On this basis, the RAD asserts that an allocation of low probative value is appropriate (RAD Decision, para.
- Evidence: `reasoning_application` cue `conclude` at chunk `4575737` offsets `466-474`; context: The RAD member further relies upon the NDP to conclude that, because the Applicant and her husband are against the practice of female genital mutilation, it is unlikely that the Applicant or her daughter will suffer this fate (RAD Decision, paras.
- Evidence: `issue` cue `issues` at chunk `4575738` offsets `31-37`; context: [15] In my view, there are two issues raised in this appeal:
Did the RAD err in its assessment of the documentary evidence?
- Evidence: `evidence_fact` cue `evidence` at chunk `4575738` offsets `114-122`; context: [15] In my view, there are two issues raised in this appeal:
Did the RAD err in its assessment of the documentary evidence?

#### Section text

II. Facts

[4] Onajite Rosemary Oranye (“the Applicant”) is a 41 year old citizen of Nigeria. She is married to “Jimmy” and there are three children of the marriage, all of whom are citizens of Nigeria: Joshua Ikechukwu Oranye (8 years old), Jordan Obinna Oranye (6 years old) and Jasmine Adaeze Oranye (4 years old).

[5] The Applicant asserts that she is a bisexual woman. She began to have feelings for both girls and boys around the age of 14, and eventually became romantically involved with one of her schoolmates, “A.” The relationship involved sexual intimacy and lasted until the time of A.’s death in 2004, when she was killed in a car accident. In her youth, she also befriended and began dating her current husband, Jimmy. In 2006, the Applicant and Jimmy broke up briefly, after the Applicant found out that he was having an affair. After the break up, the Applicant met a woman, “F.L.,” and began a relationship with her. Jimmy nevertheless continued to pursue the Applicant, and, under pressure from her family, she married him in April 2009. While married to Jimmy, the Applicant nevertheless maintained her sexual relationship with F.L. until she left Nigeria for Canada on August 20, 2016.

[6] The Applicant came to Canada in August 2016 for a vacation with her three children. Approximately one week thereafter, the Applicant’s sister “S.U.” informed the Applicant that F.L. had been arrested by the police for the offence of homosexuality, and that the police found incriminating pictures on F.L.’s laptop that might reveal their relationship. S.U. further informed the Applicant that the Nigerian police have visited her house, looking for her.

[7] Meanwhile, the Applicant’s mother informed the Applicant that Jimmy’s family wanted her and the children to return to Nigeria to undergo “ritual cleansings,” threatening that they would seek the Nigerian police’s help to track her down and even kidnap the children in order to perform the rituals. Thus, the Applicant fears that she and her children could face persecution at the hands of Jimmy’s relatives and the police should they return to Nigeria.

[8] The Applicant’s claim for protection was heard by the RPD but was denied on the grounds that the member did not find the Applicant to be credible on the core elements of her claim: notably that she is a bisexual woman and fears that she and her children could be persecuted by her husband’s family and the Nigerian police should she return.

[9] The Applicant appealed to the RAD. In a decision (“the RAD Decision”) dated June 26, 2017, the RAD upheld the RPD decision to reject the Applicant’s claim for protection. The RAD Decision forms the subject of this application for judicial review.
A. Decision Under Review

[10] The RAD Decision is organized in two parts. First, the RAD reviews the RPD’s findings with respect to the Applicant’s sexual orientation, documentary evidence, and analysis under s. 97 of the Immigration and Refugee Protection Act, SC 2001, c 27. The RAD affirms the RPD findings about the credibility of the Applicant’s oral testimony in its entirety. The RAD finds that the Applicant was not credible because of perceived hesitations, because the Applicant was unable to explain how she juggled two relationships at the same time, because the Applicant was inconsistent about whether her sexual relationship with “A.” was the only one she had without her husband’s knowledge, and because the Applicant could not explain the circumstances surrounding F.L.’s arrest (RAD Decision, para. 13).

[11] With respect to the documentary evidence, the RAD finds that the RPD approach was reasonable; notably, photographs were given little weight for lack of identifying dates or features, affidavits and other documentary evidence from Nigeria were given diminished probative value due to a lack of envelopes and spelling/typographical errors, and letters provided by Canadian LGBTQ support organizations were given diminished weight because they do not “confer sexual identity” (RAD Decision, para. 15). The RAD Decision also affirms that the RPD considered a psychological report, noting that it included information that was self-reported by the Applicant and that was contrary to the Applicant’s other evidence, and therefore appropriately accorded limited weight (RAD Decision, para. 16).

[12] The RAD further dismisses the Applicant’s argument that the RPD erred in failing to conduct a s. 97 analysis, finding that the RPD’s conclusion that the Applicant is not a bisexual woman meant that no further analysis under s. 97 was necessary to determine whether the Applicant is a person in need of protection (RAD Decision, para. 17).

[13] The second part of the RAD Decision is the “independent review of the evidence,” which focuses exclusively on the documentary evidence. The RAD Member finds the Applicant’s “recent and limited attendance at local community groups” to be unpersuasive (RAD Decision, para. 18). The RAD further finds that the letter from Dr. Devins does not necessarily corroborate the Applicant’s evidence, and that it need not be relied upon when the facts underlying it are disbelieved. The RAD, like the RPD, states that the doctor’s letter is also inconsistent with the Applicant’s other evidence (RAD Decision, para. 18).

[14] With respect to the documents from Nigeria, the RAD again affirms the observations of the RPD by noting spelling and grammar errors in the affidavits, but goes further by citing the National Documentation Package (NDP) for the proposition that fraudulent documents from Nigeria are readily available. On this basis, the RAD asserts that an allocation of low probative value is appropriate (RAD Decision, para. 19). The RAD member further relies upon the NDP to conclude that, because the Applicant and her husband are against the practice of female genital mutilation, it is unlikely that the Applicant or her daughter will suffer this fate (RAD Decision, paras. 20-21).
III. Issues

[15] In my view, there are two issues raised in this appeal:
Did the RAD err in its assessment of the documentary evidence?
Did the RPD/RAD err in assessing the Applicant’s credibility?


## 11430:3 · paragraphs 17-34

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `d4d6f4a651f0ae1da0487ef0e7dfcfa5204dede2658319902855d1fda70d0d4f`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 11430:3:subtheme:1 · paragraphs 17-18

- Raw key terms: `analysis, review, standard, accordingly, adopt, appeal, appropriate, assessment`
- Display key terms: `analysis, review, standard, accordingly, adopt, appropriate, assessment`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: analysis, review, standard, accordingly, adopt, appropriate, assessment Rule/authority context: 62 [Dunsmuir], where the appropriate standard of review is established in jurisprudence, a full analysis of the standard is unnecessary. Application context: Accordingly, I shall adopt the standard of reasonableness in the matter before me. Evidence spans paragraphs 17-18. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4575739` offsets `354-359`; context: The Federal Court of Appeal has held that the RAD is to review RPD findings of fact and mixed fact and law which raise no issue of credibility of oral evidence on a standard of correctness: Canada (Citizenship and Immigration) v.
- Evidence: `evidence_fact` cue `evidence` at chunk `4575739` offsets `383-391`; context: The Federal Court of Appeal has held that the RAD is to review RPD findings of fact and mixed fact and law which raise no issue of credibility of oral evidence on a standard of correctness: Canada (Citizenship and Immigration) v.
- Evidence: `governing_rule` cue `standard of review` at chunk `4575739` offsets `132-150`; context: 62 [Dunsmuir], where the appropriate standard of review is established in jurisprudence, a full analysis of the standard is unnecessary.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `4575739` offsets `655-666`; context: Accordingly, I shall adopt the standard of reasonableness in the matter before me.

#### 11430:3:subtheme:2 · paragraphs 19-21

- Raw key terms: `affidavits, applicant, errors, provided, argument, evidence, fraudulent, mohamud`
- Display key terms: `affidavits, errors, provided, argument, fraudulent, mohamud`
- Argument roles: `evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, party_position, reasoning_application Display terms: affidavits, errors, provided, argument, fraudulent, mohamud Position/evidence statements: [17] The Applicant submits that the RAD’s dismissal of the affidavits provided by the Applicant was erroneous. | [18] The Respondent asserts that the RPD and RAD considered the affidavits, noting that both tribunals are presumed to have considered the entire record. Application context: without an envelope) is irrelevant because affidavits are nonetheless sworn statements and should be presumed to be true absent valid and compelling reason or evidence to question their veracity. Evidence spans paragraphs 19-21. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4575740` offsets `362-370`; context: without an envelope) is irrelevant because affidavits are nonetheless sworn statements and should be presumed to be true absent valid and compelling reason or evidence to question their veracity.
- Evidence: `party_position` cue `submits` at chunk `4575740` offsets `19-26`; context: [17] The Applicant submits that the RAD’s dismissal of the affidavits provided by the Applicant was erroneous.
- Evidence: `evidence_fact` cue `evidence` at chunk `4575740` offsets `350-358`; context: without an envelope) is irrelevant because affidavits are nonetheless sworn statements and should be presumed to be true absent valid and compelling reason or evidence to question their veracity.
- Evidence: `reasoning_application` cue `because` at chunk `4575740` offsets `226-233`; context: without an envelope) is irrelevant because affidavits are nonetheless sworn statements and should be presumed to be true absent valid and compelling reason or evidence to question their veracity.
- Evidence: `party_position` cue `asserts` at chunk `4575741` offsets `20-27`; context: [18] The Respondent asserts that the RPD and RAD considered the affidavits, noting that both tribunals are presumed to have considered the entire record.
- Evidence: `evidence_fact` cue `record` at chunk `4575741` offsets `146-152`; context: [18] The Respondent asserts that the RPD and RAD considered the affidavits, noting that both tribunals are presumed to have considered the entire record.
- Evidence: `evidence_fact` cue `evidence` at chunk `4575742` offsets `57-65`; context: [19] In my view, the RAD’s assessment of the documentary evidence was unreasonable, particularly with respect to the four affidavits that were before the decision-maker.

#### 11430:3:subtheme:3 · paragraphs 22-23

- Raw key terms: `canada, envelope, envelopes, nigeria, sent, absence, affidavits, agree`
- Display key terms: `envelope, envelopes, nigeria, sent, absence, affidavits, agree`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: envelope, envelopes, nigeria, sent, absence, affidavits, agree Evidence spans paragraphs 22-23. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4575743` offsets `172-179`; context: [20] With respect to the envelopes, the RAD Decision restates the RPD member’s conclusion that “it remained unclear who sent the documents, how they arrived in Canada, and whether they came from Nigeria or not; as the Appellants also failed to provide the envelope in which they allegedly came” (RAD Decision, para.
- Evidence: `issue` cue `issue` at chunk `4575744` offsets `869-874`; context: Further, origin does not speak to authenticity – a fraudulent document can be sent legitimately by mail – but I will return to that issue later.
- Evidence: `evidence_fact` cue `record` at chunk `4575744` offsets `598-604`; context: If, for example, the RPD did not believe that the letters were truly sent by the Applicant’s cousin in Nigeria, a clear finding of fact to that end ought to have been made and supported by the evidentiary record.

#### 11430:3:subtheme:4 · paragraphs 24-28

- Raw key terms: `errors, spelling, affidavits, typographical, basis, document, documents, evidence`
- Display key terms: `errors, spelling, affidavits, typographical, basis, document, documents`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: errors, spelling, affidavits, typographical, basis, document, documents Application context: As such, I find that the decision-maker’s reasons are insufficiently transparent and must be corrected on review. Evidence spans paragraphs 24-28. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4575745` offsets `282-287`; context: Again, the RAD was satisfied with the RPD’s analysis, and in its independent examination of the evidence, the RAD similarly takes issue with the spelling and grammar errors in the affidavits.
- Evidence: `evidence_fact` cue `evidence` at chunk `4575745` offsets `248-256`; context: Again, the RAD was satisfied with the RPD’s analysis, and in its independent examination of the evidence, the RAD similarly takes issue with the spelling and grammar errors in the affidavits.
- Evidence: `issue` cue `issues` at chunk `4575746` offsets `258-264`; context: Her response noted some spelling and typographical errors, to be sure, but also included issues like inconsistent formatting of dates, difficulties with capitalization, “extra spaces” and a statement that “surprisation” is not a word.
- Evidence: `evidence_fact` cue `evidence` at chunk `4575747` offsets `378-386`; context: If a document is suspected to be fraudulent, the decision-maker must make that factual finding and ground it in the evidence; after all, an allegation of fraud is a serious accusation.
- Evidence: `counterargument_limitation` cue `However` at chunk `4575747` offsets `115-122`; context: However, in my view, holding such documents to a standard that is completely divorced from the legitimate aims of scrutiny is not to be tolerated.
- Evidence: `reasoning_application` cue `I find` at chunk `4575748` offsets `831-837`; context: As such, I find that the decision-maker’s reasons are insufficiently transparent and must be corrected on review.
- Evidence: `evidence_fact` cue `affidavit` at chunk `4575749` offsets `319-328`; context: It is important to note that each affidavit is printed on letterhead, contains the signature of the deponent, signature of a notary public, and seal.
- Evidence: `counterargument_limitation` cue `Nevertheless` at chunk `4575749` offsets `633-645`; context: Nevertheless, the RAD uses the NDP to justify a decision to accord “low probative value” to the documents.

#### 11430:3:subtheme:5 · paragraphs 29-30

- Raw key terms: `affidavits, applicant, approach, authenticity, decision, document, documents, fact`
- Display key terms: `affidavits, approach, authenticity, document, documents, fact`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue Display terms: affidavits, approach, authenticity, document, documents, fact Rule/authority context: In my view, such an approach is prejudicial and should not be tolerated in our jurisprudence. Evidence spans paragraphs 29-30. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4575750` offsets `1217-1222`; context: While the RAD has tried to mix the issue of fraudulent documents with “cumulative credibility concerns and [an] overall lack of credibility” on the part of the Applicant, the credibility of the Applicant’s oral testimony has nothing to do with the authenticity of the affidavits in question.
- Evidence: `evidence_fact` cue `evidence` at chunk `4575750` offsets `112-120`; context: They cannot mask authenticity findings by simply deeming evidence to be of “little probative value.
- Evidence: `issue` cue `question` at chunk `4575751` offsets `338-346`; context: While the RAD Decision casts doubt on the authenticity of the four affidavits through a simple reference to information contained in the NDP, it provides no analysis as to how the “easy availability” of fraudulent documents in Nigeria connects to the question as to whether these affidavits are fraudulent.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4575751` offsets `1162-1175`; context: In my view, such an approach is prejudicial and should not be tolerated in our jurisprudence.
- Evidence: `counterargument_limitation` cue `however` at chunk `4575751` offsets `611-618`; context: It does not, however, say anything about how one might identify a fraudulent document (e.

#### 11430:3:subtheme:6 · paragraphs 31-32

- Raw key terms: `evidence, above, accord, affidavits, alert, alternative, amounts, analysis`
- Display key terms: `above, accord, affidavits, alert, alternative, amounts, analysis`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: above, accord, affidavits, alert, alternative, amounts, analysis Application context: [30] As should be clear from the above discussion, I find that the RAD’s analysis of the Applicant’s documentary evidence, specifically the four affidavits provided by the Applicant, was unreasonable. Evidence spans paragraphs 31-32. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4575752` offsets `318-323`; context: Where they appear in country condition documents, these generalizations can only properly serve to alert the decision-maker to the issue.
- Evidence: `evidence_fact` cue `evidence` at chunk `4575752` offsets `168-176`; context: [29] It is unfortunate that generalizations about the “easy availability of fraudulent documents” are frequently relied upon as though they constitute incontrovertible evidence of fraud.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `4575752` offsets `374-380`; context: The finding about the authenticity of a document cannot depend or even be influenced by mere suspicion from the reputation of a given country.
- Evidence: `evidence_fact` cue `evidence` at chunk `4575753` offsets `113-121`; context: [30] As should be clear from the above discussion, I find that the RAD’s analysis of the Applicant’s documentary evidence, specifically the four affidavits provided by the Applicant, was unreasonable.
- Evidence: `reasoning_application` cue `I find` at chunk `4575753` offsets `51-57`; context: [30] As should be clear from the above discussion, I find that the RAD’s analysis of the Applicant’s documentary evidence, specifically the four affidavits provided by the Applicant, was unreasonable.

#### 11430:3:subtheme:7 · paragraphs 33-34

- Raw key terms: `certification, arising, asked, assessment, concur, counsel, deal, determined`
- Display key terms: `certification, arising, asked, assessment, concur, deal, determined`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: certification, arising, asked, assessment, concur, deal, determined Evidence spans paragraphs 33-34. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4575754` offsets `131-136`; context: [31] Having determined that the RAD’s assessment of the documentary evidence was unreasonable, it is unnecessary to deal with this issue.
- Evidence: `evidence_fact` cue `determined that` at chunk `4575754` offsets `12-27`; context: [31] Having determined that the RAD’s assessment of the documentary evidence was unreasonable, it is unnecessary to deal with this issue.

#### Section text

IV. Analysis
A. Standard of Review

[16] As the Supreme Court of Canada explained in Dunsmuir v New Brunswick, 2008 SCC 9 at para. 62 [Dunsmuir], where the appropriate standard of review is established in jurisprudence, a full analysis of the standard is unnecessary. The Federal Court of Appeal has held that the RAD is to review RPD findings of fact and mixed fact and law which raise no issue of credibility of oral evidence on a standard of correctness: Canada (Citizenship and Immigration) v. Huruglica, 2016 FCA 93 [Huruglica] at para. 103. The Federal Court of Appeal furthermore held that this Court is to review RAD decisions on a standard of reasonableness: Huruglica at para. 35. Accordingly, I shall adopt the standard of reasonableness in the matter before me.
B. RAD Assessment of the Documentary Evidence

[17] The Applicant submits that the RAD’s dismissal of the affidavits provided by the Applicant was erroneous. The Applicant argues that the manner in which the affidavits were received (ie. without an envelope) is irrelevant because affidavits are nonetheless sworn statements and should be presumed to be true absent valid and compelling reason or evidence to question their veracity. In oral argument, the Applicant relied upon this Court’s recent decision in Mohamud v. Canada (Citizenship and Immigration), 2018 FC 170 [Mohamud] for the proposition that minor clerical errors are not a proper basis for characterizing an affidavit as fraudulent.

[18] The Respondent asserts that the RPD and RAD considered the affidavits, noting that both tribunals are presumed to have considered the entire record. In oral argument, the Respondent distinguished Mohamud from the case at bar, arguing that the multiplicity of errors in the affidavits provided by the Applicant are not comparable to the single error that was present in Mohamud.

[19] In my view, the RAD’s assessment of the documentary evidence was unreasonable, particularly with respect to the four affidavits that were before the decision-maker. There are essentially three reasons advanced by the RPD to accord them a finding of low probative value: 1) original envelopes were not provided by the Applicant, 2) the affidavits contain spelling and grammar errors, and 3) fraudulent documents are widely available in Nigeria. I shall address each in turn.
(1) Envelopes

[20] With respect to the envelopes, the RAD Decision restates the RPD member’s conclusion that “it remained unclear who sent the documents, how they arrived in Canada, and whether they came from Nigeria or not; as the Appellants also failed to provide the envelope in which they allegedly came” (RAD Decision, para. 16). The RAD was satisfied with the RPD’s findings on this point.

[21] I cannot agree. The only thing that a mailing envelope illustrates is a document’s provenance; however, in this case, the affidavits are presumably of interest for their content, not their origin. The affidavits’ origins and method of arrival in Canada would only be of interest if the RPD suspected that the Applicant was lying about them, which would go to the Applicant’s credibility. If, for example, the RPD did not believe that the letters were truly sent by the Applicant’s cousin in Nigeria, a clear finding of fact to that end ought to have been made and supported by the evidentiary record. Here, the RPD made no such finding, and I cannot discern why the absence of the mailing envelopes was relevant to the RPD and RAD. Further, origin does not speak to authenticity – a fraudulent document can be sent legitimately by mail – but I will return to that issue later.
(2) Spelling and Grammar

[22] The RPD noted that two of the affidavits provided by the Applicant were “full” of spelling and grammar mistakes and also had typographical errors. Again, the RAD was satisfied with the RPD’s analysis, and in its independent examination of the evidence, the RAD similarly takes issue with the spelling and grammar errors in the affidavits. The RAD Decision notes that its finding is “in accordance with settled law,” and then cites a lengthy quote in support of the point (RAD Decision, para. 19). Regrettably, the RAD member forgot to provide a citation in what, I am certain, was an inadvertent typographical error.

[23] The irony here is difficult to miss, and yet there is more. In oral argument, I asked the Respondent’s counsel to point out the offending errors in the affidavits. Her response noted some spelling and typographical errors, to be sure, but also included issues like inconsistent formatting of dates, difficulties with capitalization, “extra spaces” and a statement that “surprisation” is not a word. It goes without saying that these are an exceptionally trivial basis upon which to find fault with the authenticity of a foreign document. Also, while the word “surprisation” does not appear in the Oxford English Dictionary, it is used in Nigerian English: see D. Jowitt, “The Fall-Rise in Nigerian English Intonation”, in O. Ndimele, ed., Convergence: English & Nigerian Languages (2016), 9, at p. 35.

[24] I underline these points not to diminish the important task of scrutinizing legal documents for authenticity. However, in my view, holding such documents to a standard that is completely divorced from the legitimate aims of scrutiny is not to be tolerated. If a document is suspected to be fraudulent, the decision-maker must make that factual finding and ground it in the evidence; after all, an allegation of fraud is a serious accusation. However, a handful of spelling, grammar and typographical errors cannot suffice. Moreover, the RPD and RAD’s approach must be sensitive to the fact that foreign documents may not follow the same customs, traditions, and language conventions that are familiar in Canada. Those contextual differences cannot be the basis upon which to ground a finding of fraud.

[25] In the case at bar, there were four affidavits, and yet the RPD cited spelling, grammar, and typographical defects in only two of them. One must ask: why was no mention made of the other two affidavits in the RPD and RAD decisions? The Applicant cannot know based on the reasons provided, despite the fact that the other two affidavits do not contain such errors. Typographical errors and spelling/grammar mistakes in two out of the four documents is not an appropriate basis to sweepingly assign “low probative value” to all four affidavits. This is especially true when one considers that the content of all four affidavits is consistent and corroborates the core of the Applicant’s claims – that is, as a result of her sexual orientation being exposed, the Applicant and her children are in danger of persecution. As such, I find that the decision-maker’s reasons are insufficiently transparent and must be corrected on review.
(3) Fraudulent Documents

[26] In its independent assessment of the affidavits, the RAD relies upon the Nigeria NDP for the proposition that fraudulent documents are easily available in Nigeria. No further analysis is provided, and the RAD makes no factual finding that the affidavits are, in fact, fraudulent. It is important to note that each affidavit is printed on letterhead, contains the signature of the deponent, signature of a notary public, and seal. Three of the four affidavits are accompanied by a piece of identification belonging to the respective deponent, each of which contains a signature that can be used for the purposes of verification. Nevertheless, the RAD uses the NDP to justify a decision to accord “low probative value” to the documents. I shall reproduce the RAD finding to illustrate the point:
In light of the cumulative credibility concerns and overall lack of credibility, as set out earlier; and also the fact that the documentary evidence in the National Documentation Package (NDP) describes the easy availability of fraudulent documents from the Appellants’ country, as well as the spelling and grammatical errors in the document themselves, the RAD also gives little probative value to the documents purportedly sent by Jimmy’s family in Nigeria.
[Citation omitted]
[RAD Decision, para. 19]

[27] Fact finders must have the courage to find facts. They cannot mask authenticity findings by simply deeming evidence to be of “little probative value.” As Justice Mactavish so rightly put it in Sitnikova v. Canada (Citizenship and Immigration), 2017 FC 1082 at para. 20, which I will reproduce in its entirety:
This Court has, moreover, previously commented on the practice of decision-makers giving “little weight” to documents without making an explicit finding as to their authenticity: see, for example, Marshall v. Canada (Citizenship and Immigration), 2009 FC 622 (CanLII) at paras. 1-3, [2009] F.C.J. No. 799 and Warsame v. Canada (Minister of Employment and Immigration), [1993] F.C.J. No. 1202, at para. 10. If a decision-maker is not convinced of the authenticity of a document, then they should say so and give the document no weight whatsoever. Decision‑makers should not cast aspersions on the authenticity of a document, and then endeavour to hedge their bets by giving the document “little weight”. As Justice Nadon observed in Warsame, “[i]t is all or nothing”: at para. 10.
This improper approach is precisely the one employed by the RAD in the case before me. While the RAD has tried to mix the issue of fraudulent documents with “cumulative credibility concerns and [an] overall lack of credibility” on the part of the Applicant, the credibility of the Applicant’s oral testimony has nothing to do with the authenticity of the affidavits in question. It is either the affidavits are authentic or fraudulent, but the RAD makes no finding on the point and instead opts to “hedge” by according them little probative value. This is an error of law.

[28] Unfortunately, the problems with the RAD’s independent analysis do not end there. While the RAD Decision casts doubt on the authenticity of the four affidavits through a simple reference to information contained in the NDP, it provides no analysis as to how the “easy availability” of fraudulent documents in Nigeria connects to the question as to whether these affidavits are fraudulent. There is good reason for that. The NDP discusses the laws in Nigeria governing fraudulent documents, instances of their use domestically and internationally, and efforts taken to crack down on their use. It does not, however, say anything about how one might identify a fraudulent document (e.g. stamps, seals, spelling/grammatical/typographical errors) that could be used to evaluate the affidavits provided by the Applicant. In other words, the NDP contains no information to lead to the conclusion that these affidavits are fraudulent; the only link between the NDP and the affidavits tendered by the Applicant is the fact that she is Nigerian and her documents originate from Nigeria. In my view, such an approach is prejudicial and should not be tolerated in our jurisprudence.

[29] It is unfortunate that generalizations about the “easy availability of fraudulent documents” are frequently relied upon as though they constitute incontrovertible evidence of fraud. Where they appear in country condition documents, these generalizations can only properly serve to alert the decision-maker to the issue. The finding about the authenticity of a document cannot depend or even be influenced by mere suspicion from the reputation of a given country. Each document must be analyzed individually and its authenticity decided on its own merits. If there is evidence of fraud, it speaks for itself and the decision-maker should accord it no probative value. The alternative – that is, relying on the prevalence of fraud in a given country to impugn the authenticity of a document – amounts to finding guilt by association.

[30] As should be clear from the above discussion, I find that the RAD’s analysis of the Applicant’s documentary evidence, specifically the four affidavits provided by the Applicant, was unreasonable. On this basis, the decision must be returned for redetermination.
C. RPD/RAD err in assessing the Applicant’s credibility

[31] Having determined that the RAD’s assessment of the documentary evidence was unreasonable, it is unnecessary to deal with this issue.
V. Certification

[32] Counsel for both parties were asked if there were questions requiring certification, they each stated that there were no questions arising for certification and I concur.


## 11430:4 · paragraphs 35-36

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `5f6a9ec76dd92e08308ae48925f6c1c8da3e5e6659ca3f6089d24974ec0c0e44`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 11430:4:subtheme:1 · paragraphs 35-36

- Raw key terms: `imm-3178-17, judgment, adaeze, ahmed, appearances, applicants, april, aside`
- Display key terms: `imm-3178-17, adaeze, ahmed, april, aside`
- Argument roles: `governing_rule, issue`
- Explanation: Observed roles: governing_rule, issue Display terms: imm-3178-17, adaeze, ahmed, april, aside Rule/authority context: JUDGMENT in IMM-3178-17 THIS COURT’S JUDGMENT is that: The decision under review is set aside and the matter referred back for redetermination by a differently constituted panel. Evidence spans paragraphs 35-36. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4575755` offsets `367-375`; context: There is no question to certify.
- Evidence: `governing_rule` cue `under` at chunk `4575755` offsets `244-249`; context: JUDGMENT in IMM-3178-17
THIS COURT’S JUDGMENT is that:
The decision under review is set aside and the matter referred back for redetermination by a differently constituted panel.

#### Section text

JUDGMENT in IMM-3178-17
THIS COURT’S JUDGMENT is that:
The decision under review is set aside and the matter referred back for redetermination by a differently constituted panel.
There is no question to certify.
"Shirzad A."
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET:
IMM-3178-17
STYLE OF CAUSE:
ONAJITE ROSEMARY ORANYE, JOSHUA IKECHUKWU ORANYE (MINOR), JORDAN OBINNA ORANYE (MINOR), JASMIN ADAEZE ORANYE (MINOR) v THE MINISTER OF CITIZENSHIP AND IMMIGRATION
PLACE OF HEARING:
Toronto, Ontario
DATE OF HEARING:
FEBRUARY 28, 2018
JUDGMENT AND REASONS:
AHMED J.
DATED:
APRIL 11, 2018
APPEARANCES:
Ms. Oluwakemi Oduwole
For The Applicants
Marcia Pritzker Schmitt
For The Respondent
SOLICITORS OF RECORD:
Topmarké Attorneys LLP
Barristers and Solicitors
Toronto, Ontario
For The Applicants
Attorney General of Canada
Toronto, Ontario
For The Respondent
