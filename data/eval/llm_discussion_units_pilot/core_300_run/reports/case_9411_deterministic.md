# Discussion Units: case 9411

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **31**
- Continuity pairs: **30**
- Discussion Units: **3**
- Paragraph source hashes: **31**
- Sub-themes: **8**

## 9411:1 · paragraphs 0-27

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `1ad0b6b6f1e3d6ebb9592d174b41d0d1b6daf3fa114d5b4463c995110908e23b`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 9411:1:subtheme:1 · paragraphs 0-14

- Raw key terms: `applicant, haiti, decision, following, found, relationship, because, family`
- Display key terms: `haiti, following, relationship, because, family`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: haiti, following, relationship, because, family Position/evidence statements: Surprisingly, the applicant claimed that her family learned of her homosexuality that same day in 2015. | [6] As a result, the applicant left the family home to live with a friend, a woman, in a different area, but she claims that the threats against her continued. Rule/authority context: It is made pursuant to section 72 of the Immigration and Refugee Protection Act, SC 2001, c 27. Application context: Edmond, a citizen of Haiti, claims that she fears that she would be persecuted because of her sexual orientation in her country of nationality. | However, they hid their relationship because of the discrimination and stigmatization resulting from homosexuality in Haiti. Evidence spans paragraphs 0-14. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4476022` offsets `308-313`; context: The only issue turns on the credibility of this applicant.
- Evidence: `evidence_fact` cue `found that` at chunk `4476022` offsets `366-376`; context: The RPD found that it constituted the determinative issue.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4476022` offsets `136-147`; context: It is made pursuant to section 72 of the Immigration and Refugee Protection Act, SC 2001, c 27.
- Evidence: `reasoning_application` cue `because` at chunk `4476023` offsets `87-94`; context: Edmond, a citizen of Haiti, claims that she fears that she would be persecuted because of her sexual orientation in her country of nationality.
- Evidence: `counterargument_limitation` cue `However` at chunk `4476023` offsets `256-263`; context: However, that relationship deteriorated and he physically abused her and even threatened at some point to kill her if she left him.
- Evidence: `reasoning_application` cue `because` at chunk `4476024` offsets `272-279`; context: However, they hid their relationship because of the discrimination and stigmatization resulting from homosexuality in Haiti.
- Evidence: `counterargument_limitation` cue `However` at chunk `4476024` offsets `235-242`; context: However, they hid their relationship because of the discrimination and stigmatization resulting from homosexuality in Haiti.
- Evidence: `party_position` cue `claimed` at chunk `4476025` offsets `473-480`; context: Surprisingly, the applicant claimed that her family learned of her homosexuality that same day in 2015.
- Evidence: `party_position` cue `claims` at chunk `4476026` offsets `113-119`; context: [6] As a result, the applicant left the family home to live with a friend, a woman, in a different area, but she claims that the threats against her continued.
- Evidence: `evidence_fact` cue `found that` at chunk `4476027` offsets `1139-1149`; context: In conclusion, the panel found that the applicant did not face a risk of persecution should she return to Haiti.
- Evidence: `evidence_fact` cue `found that` at chunk `4476028` offsets `122-132`; context: The RPD found that the testimony of the applicant was vague, considering the type of relationship she alleges she has with that person.
- Evidence: `evidence_fact` cue `record` at chunk `4476029` offsets `95-101`; context: [10] Furthermore, the short letter of support from the alleged companion, which is part of the record, is again presented as not being very detailed, merely speaking in general terms of threats and violence suffered in Haiti.
- Evidence: `reasoning_application` cue `because` at chunk `4476029` offsets `416-423`; context: While the applicant testified that in general terms her companion loved her because of the things she did for her and the way she talked to her, the letter is slightly more specific with respect to physical contacts and to the allegation that “she came to her with arguments to show the claimant that she could be happy with [the companion]” (para 10 of the RPD’s decision).
- Evidence: `party_position` cue `claimed` at chunk `4476030` offsets `94-101`; context: [11] The RPD was also struck by the lack of evidence of the communications that the applicant claimed she has continued to have with her companion since her arrival in Canada.
- Evidence: `evidence_fact` cue `evidence` at chunk `4476030` offsets `44-52`; context: [11] The RPD was also struck by the lack of evidence of the communications that the applicant claimed she has continued to have with her companion since her arrival in Canada.
- Evidence: `reasoning_application` cue `because` at chunk `4476030` offsets `433-440`; context: Why she continued in that way in spite of the very different circumstances in Canada, and her claim that she was afraid to go back to Haiti because of her homosexuality, is somewhat puzzling.
- Evidence: `evidence_fact` cue `evidence` at chunk `4476031` offsets `164-172`; context: The RPD expressed concerns about the lack of evidence on the part of the applicants’ siblings with respect to an incident that allegedly took place at their house while they were there.
- Evidence: `reasoning_application` cue `because` at chunk `4476031` offsets `842-849`; context: That person did not provide any evidence in support and the panel was less than impressed because “the claimant provided no further details as to why they are not speaking and has not provided a reasonable explanation for why she could not have obtained a letter from [that person]” (para 19, RPD’s decision).
- Evidence: `evidence_fact` cue `testimony` at chunk `4476032` offsets `24-33`; context: [13] On the applicant’s testimony about that incident, the RPD notes that this constitutes the only incident of violence that is alleged by the applicant.
- Evidence: `party_position` cue `claims` at chunk `4476033` offsets `847-853`; context: The simple fact that the applicant did not have her passport does not explain why she claims she was forced to return to Haiti following the internship.
- Evidence: `counterargument_limitation` cue `Nevertheless` at chunk `4476033` offsets `267-279`; context: Nevertheless, she did not seek asylum in the U.
- Evidence: `party_position` cue `claims` at chunk `4476035` offsets `506-512`; context: Similarly, there was an expectation that there would have been provided a fuller explanation about the reaction of her family when, as she claims, they found out about her sexual orientation following the May 2015 incident when, according to the applicant, she had already been the subject of harassment in the community for a few years.

#### 9411:1:subtheme:2 · paragraphs 15-17

- Raw key terms: `assessment, canada, citizenship, court, credibility, credible, evidence, facts`
- Display key terms: `assessment, credibility, credible, facts`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: assessment, credibility, credible, facts Rule/authority context: Standard of review [18] The only issue in this case is whether or not the story told by the applicant carries weight in view of the credibility assessment conducted by the RPD. Application context: The letter cannot, therefore, support the applicant’s contention. | In their treatise, The Law of Evidence, 7th ed (Toronto: Irwin law, 2015), the authors David Paciocco and Lee Stuesser state: In general, the trier of fact is entitled simply to apply common sense and human experience in Evidence spans paragraphs 15-17. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4476036` offsets `547-552`; context: Standard of review [18] The only issue in this case is whether or not the story told by the applicant carries weight in view of the credibility assessment conducted by the RPD.
- Evidence: `evidence_fact` cue `evidence` at chunk `4476036` offsets `433-441`; context: In a word, it is not independent evidence.
- Evidence: `governing_rule` cue `Standard of review` at chunk `4476036` offsets `514-532`; context: Standard of review [18] The only issue in this case is whether or not the story told by the applicant carries weight in view of the credibility assessment conducted by the RPD.
- Evidence: `reasoning_application` cue `therefore` at chunk `4476036` offsets `462-471`; context: The letter cannot, therefore, support the applicant’s contention.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `4476036` offsets `454-460`; context: The letter cannot, therefore, support the applicant’s contention.
- Evidence: `issue` cue `whether` at chunk `4476037` offsets `881-888`; context: In their treatise, The Law of Evidence, 7th ed (Toronto: Irwin law, 2015), the authors David Paciocco and Lee Stuesser state:
In general, the trier of fact is entitled simply to apply common sense and human experience in determining whether evidence is credible and in deciding what use, if any, to make of it in coming to its finding of fact.
- Evidence: `evidence_fact` cue `Evidence` at chunk `4476037` offsets `678-686`; context: In their treatise, The Law of Evidence, 7th ed (Toronto: Irwin law, 2015), the authors David Paciocco and Lee Stuesser state:
In general, the trier of fact is entitled simply to apply common sense and human experience in determining whether evidence is credible and in deciding what use, if any, to make of it in coming to its finding of fact.
- Evidence: `reasoning_application` cue `apply` at chunk `4476037` offsets `826-831`; context: In their treatise, The Law of Evidence, 7th ed (Toronto: Irwin law, 2015), the authors David Paciocco and Lee Stuesser state:
In general, the trier of fact is entitled simply to apply common sense and human experience in determining whether evidence is credible and in deciding what use, if any, to make of it in coming to its finding of fact.

#### 9411:1:subtheme:3 · paragraphs 18-19

- Raw key terms: `assessment, canada, citizenship, credibility, immigration, adverse, applicant, attakora`
- Display key terms: `assessment, credibility, adverse, attakora`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue Display terms: assessment, credibility, adverse, attakora Rule/authority context: [15] The principles governing the assessment of an applicant’s credibility in the refugee context are well-established within this Court. Evidence spans paragraphs 18-19. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4476039` offsets `407-413`; context: Adverse credibility findings should however not be based on a microscopic evaluation of issues peripheral or irrelevant to the case (Attakora v Canada (Minister of Employment and Immigration), [1989] FCJ No 444).
- Evidence: `evidence_fact` cue `evidence` at chunk `4476039` offsets `587-595`; context: In effect, the RPD has to consider the entirety of the evidence.
- Evidence: `governing_rule` cue `principles` at chunk `4476039` offsets `9-19`; context: [15] The principles governing the assessment of an applicant’s credibility in the refugee context are well-established within this Court.
- Evidence: `counterargument_limitation` cue `however` at chunk `4476039` offsets `355-362`; context: Adverse credibility findings should however not be based on a microscopic evaluation of issues peripheral or irrelevant to the case (Attakora v Canada (Minister of Employment and Immigration), [1989] FCJ No 444).

#### 9411:1:subtheme:4 · paragraphs 20-24

- Raw key terms: `applicant, canada, testimony, because, clear, court, credible, details`
- Display key terms: `testimony, because, clear, credible, details`
- Argument roles: `evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, reasoning_application Display terms: testimony, because, clear, credible, details Application context: Third, the RPD is recognized to have expertise in assessing refugee claims and is authorized by statute to apply its specialized knowledge: Chen v Canada (Minister of Citizenship and Immigration), 2003 FCT 805 at para 10 | [26] While the applicant borrows money to attend an internship in Miami, Florida, which would allow her to escape her fear of death in Haiti, she returns to Haiti because her passport was kept by the organizers during th Evidence spans paragraphs 20-24. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4476041` offsets `1625-1631`; context: Third, it is well-established that the RPD may make credibility findings based on implausibility, common sense and rationality, although adverse credibility findings “should not be based on a microscopic evaluation of issues peripheral or irrelevant to the case”: Haramichael v Canada (Minister of Citizenship and Immigration), 2016 FC 1197 at para 15, Tremblay-Lamer J, citing Lubana v Canada (Minister of Citizenship and Immigration), 2003 FCT 116 at paras 10-11, Martineau J [Lubana]; Attakora v Canada (Minister of Employment and Immigration), [1989] FCJ No 444 (FCA).
- Evidence: `evidence_fact` cue `evidence` at chunk `4476041` offsets `158-166`; context: First, the RPD has broad discretion to prefer certain evidence over other evidence and to determine the weight to be assigned to the evidence it accepts: Medarovik v Canada (Minister of Citizenship and Immigration), 2002 FCT 61 at para 16, Tremblay-Lamer, J; Pushpanathan v Canada (Minister of Citizenship and Immigration), 2002 FCT 867 at para 68, Blais J.
- Evidence: `reasoning_application` cue `apply` at chunk `4476041` offsets `815-820`; context: Third, the RPD is recognized to have expertise in assessing refugee claims and is authorized by statute to apply its specialized knowledge: Chen v Canada (Minister of Citizenship and Immigration), 2003 FCT 805 at para 10, O’Reilly, J; and see Siad v Canada (Secretary of State), [1997] 1 FC 608 at para 24 (FCA), where the Federal Court of Appeal said that the RPD, “… is uniquely situated to assess the credibility of a refugee claimant; credibility determinations, which lie within “the heartland of the discretion of triers of fact”, are entitled to considerable deference upon judicial review and cannot be overturned unless they are perverse, capricious or made without regard to the evidence.
- Evidence: `evidence_fact` cue `testimony` at chunk `4476042` offsets `418-427`; context: I have read carefully the transcript of the testimony given by the applicant before the RPD and come to the conclusion that the outcome falls within the range of acceptable, possible outcomes and the decision has been amply justified.
- Evidence: `evidence_fact` cue `evidence` at chunk `4476043` offsets `122-130`; context: [24] It was open for the RPD to consider the narrative as being implausible and the applicant less than credible when the evidence is examined in its entirety.
- Evidence: `evidence_fact` cue `testimony` at chunk `4476044` offsets `223-232`; context: The RPD noted the discrepancies between some aspects of the letter and the applicant’s testimony, in spite of its lack of details.
- Evidence: `reasoning_application` cue `because` at chunk `4476045` offsets `163-170`; context: [26] While the applicant borrows money to attend an internship in Miami, Florida, which would allow her to escape her fear of death in Haiti, she returns to Haiti because her passport was kept by the organizers during the internship and she does not speak English.

#### 9411:1:subtheme:5 · paragraphs 25-26

- Raw key terms: `evidence, findings, within, acceptable, administrative, amounts, ample, answers`
- Display key terms: `findings, within, acceptable, administrative, amounts, ample, answers`
- Argument roles: `evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, reasoning_application Display terms: findings, within, acceptable, administrative, amounts, ample, answers Application context: That does not suggest that every time the RPD concludes on a matter of credibility that the conclusion becomes reasonable. | [28] In the case at bar, I find that there was considerable evidence to support the findings. Evidence spans paragraphs 25-26. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4476046` offsets `234-240`; context: In so doing, counsel conducted the same kind of microscopic evaluation of issues that is often complained about when done by administrative tribunals.
- Evidence: `evidence_fact` cue `evidence` at chunk `4476046` offsets `512-520`; context: Indeed, it is the entirety of the evidence available on this record that must be assessed, applying common sense and human experience.
- Evidence: `reasoning_application` cue `concludes` at chunk `4476046` offsets `786-795`; context: That does not suggest that every time the RPD concludes on a matter of credibility that the conclusion becomes reasonable.
- Evidence: `evidence_fact` cue `evidence` at chunk `4476047` offsets `60-68`; context: [28] In the case at bar, I find that there was considerable evidence to support the findings.
- Evidence: `reasoning_application` cue `I find` at chunk `4476047` offsets `25-31`; context: [28] In the case at bar, I find that there was considerable evidence to support the findings.

#### 9411:1:subtheme:6 · paragraphs 27-27

- Raw key terms: `application, certified, dismissed, judicial, question, result, review`
- Display key terms: `certified, dismissed, judicial, question, result, review`
- Argument roles: `disposition, issue`
- Explanation: Observed roles: disposition, issue Display terms: certified, dismissed, judicial, question, result, review Operative outcome context: [29] As a result, the judicial review application must be dismissed. Evidence spans paragraphs 27-27. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4476048` offsets `91-99`; context: There is no certified question.
- Evidence: `disposition` cue `dismissed` at chunk `4476048` offsets `58-67`; context: [29] As a result, the judicial review application must be dismissed.

#### Section text

Edmond v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2017-07-04
Neutral citation
2017 FC 644
File numbers
IMM-112-17
Decision Content
Date: 20170704
Docket: IMM-112-17
Citation: 2017 FC 644
Ottawa, Ontario, July 4, 2017
PRESENT: The Honourable Mr. Justice Roy
BETWEEN:
MARIE NERLANDE EDMOND
Applicant
and
MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
JUDGMENT AND REASONS

[1] This judicial review application is from a decision of the Refugee Protection Division [RPD], made on November 18, 2016. It is made pursuant to section 72 of the Immigration and Refugee Protection Act, SC 2001, c 27. The RPD refused the applicant as a refugee or a person in need of protection. The only issue turns on the credibility of this applicant. The RPD found that it constituted the determinative issue.

[2] Ms. Edmond, a citizen of Haiti, claims that she fears that she would be persecuted because of her sexual orientation in her country of nationality.
I. The facts [3] The applicant was born in Haiti in 1984. In 2005, she began a relationship with a man. However, that relationship deteriorated and he physically abused her and even threatened at some point to kill her if she left him. Hence, the relationship ended in 2008.

[4] One of the applicant’s childhood friends helped the applicant during her abusive relationship and became the applicant’s confidante. The applicant declares that she fell in love with that woman and declared her love in March 2010. However, they hid their relationship because of the discrimination and stigmatization resulting from homosexuality in Haiti. It seems that in some segments of the population, the terrible earthquake of 2010 is blamed on homosexuals who would have brought onto the country the wrath of God.

[5] Starting in 2013, others in the neighbourhood would have noticed the relationship and insults followed. On May 19, 2015, the applicant and her family were attacked at their house by a mob throwing stones. They threatened to burn down the house if the applicant did not leave the neighbourhood. In spite of a complaint lodged by the applicant’s brother the following day, there was no follow-up by the police other than a visit to the house. Surprisingly, the applicant claimed that her family learned of her homosexuality that same day in 2015.

[6] As a result, the applicant left the family home to live with a friend, a woman, in a different area, but she claims that the threats against her continued. She moved into an apartment with her two sisters in October 2015.

[7] The applicant obtained a visa to travel to the United States (U.S.) in April 2016 for a 15-day internship at a college in Miami. The applicant is trained as a nurse, but it seems that she never practiced as such. Following the internship, she returned to Haiti and then fled to New-York on June 18, 2016, using the same U.S. visa. Two months later, on August 2, 2016, the applicant made her way to the Canadian border all the way across New York State, at Fort Erie. She made a refugee claim and lived with her sister who is already a permanent resident and lives in the Toronto area. The refugee claim was filed on August 13, 2016.
II. The RPD’s decision [8] Basically, the RPD did not believe the applicant. It did not believe that she was in a romantic relationship with another woman, that her family was attacked in May 2015, or that she is homosexual. The RPD also drew negative inferences from the applicant’s re-availment to Haiti in 2016, and her failure to claim asylum in the United-States. In fact, there were two opportunities to seek asylum, but the applicant declared that she preferred Canada. In conclusion, the panel found that the applicant did not face a risk of persecution should she return to Haiti.

[9] The first pillar in the decision relates to the applicant’s relationship with her alleged companion in Haiti. The RPD found that the testimony of the applicant was vague, considering the type of relationship she alleges she has with that person. Thus, the expectation was that the applicant would provide more detailed answers regarding that person, which did not materialize. In the view of the RPD, the testimony was generic. On questions as specific as how comfort and support were forthcoming following the applicant’s break-up with her boyfriend, the answers were at best generic. Similarly, the RPD commented on the lack of specificity of activities that they would be conducting together.

[10] Furthermore, the short letter of support from the alleged companion, which is part of the record, is again presented as not being very detailed, merely speaking in general terms of threats and violence suffered in Haiti. The RPD noted that the letter is not completely consistent with the applicant’s testimony on an important aspect. While the applicant testified that in general terms her companion loved her because of the things she did for her and the way she talked to her, the letter is slightly more specific with respect to physical contacts and to the allegation that “she came to her with arguments to show the claimant that she could be happy with [the companion]” (para 10 of the RPD’s decision).

[11] The RPD was also struck by the lack of evidence of the communications that the applicant claimed she has continued to have with her companion since her arrival in Canada. The applicant explained that she deleted all of her correspondence with her girlfriend as it was her habit in Haiti. Why she continued in that way in spite of the very different circumstances in Canada, and her claim that she was afraid to go back to Haiti because of her homosexuality, is somewhat puzzling. In the view of the RPD, that is simply not reasonable.

[12] Another pillar of the decision is the story told around the incident of May 19, 2015, according to the applicant. The RPD expressed concerns about the lack of evidence on the part of the applicants’ siblings with respect to an incident that allegedly took place at their house while they were there. The only explanation provided by the applicant was that she did not ask for that kind of supporting evidence. That concern is amplified due to the fact that some documents would appear to have been sent from Haiti by the applicant’s brother, without even an attempt at testifying through an affidavit or a letter. The same kind of concern comes to the fore about the applicant going to live with another woman following the May 19, 2015 incident. That person did not provide any evidence in support and the panel was less than impressed because “the claimant provided no further details as to why they are not speaking and has not provided a reasonable explanation for why she could not have obtained a letter from [that person]” (para 19, RPD’s decision).

[13] On the applicant’s testimony about that incident, the RPD notes that this constitutes the only incident of violence that is alleged by the applicant. Yet, she was unable, or unwilling, to speak about the reactions of her siblings at the fact that people were, according to the applicant, stoning their home. Thus, on the balance of probabilities, the RPD found that the claimant did not establish that the May 19, 2015 incident occurred or “that it was in relation to her alleged sexual orientation” (para 23, RPD’s decision).

[14] The RPD also found against the applicant with respect to her internship in Miami, Florida, from May 2 to May 15, 2016. The internship, financed with borrowed money, was presented by the applicant as being an opportunity for her since she was in danger in Haiti. Nevertheless, she did not seek asylum in the U.S. on that occasion, claiming that her passport would have been kept by the organizers. She also indicated that she did not speak English. The RPD considered that this applicant, who is a sophisticated person, with a degree in nursing and already 32 years of age at the time of the internship, did not justify not seeking assistance while in Miami and while, at the same time, claiming that she feared for her life if she were to return to Haiti. The simple fact that the applicant did not have her passport does not explain why she claims she was forced to return to Haiti following the internship. Indeed, she still did not speak English a month later when she arrived in New York, or two months later when she crossed the border into Southern Ontario.

[15] As the RPD noted, the explanation is particularly thin “given that she was not illegally in the U.S. at that point, and that she returned to the U.S. in order to come to Canada where she has family a month later” (para 26).

[16] Furthermore, the RPD noted the reluctance of the applicant to answer questions relating to her sexual orientation and the persecution she suffered as a result. Thus, the RPD held against the applicant that she was not able to answer questions directly, repeatedly, regarding the impact keeping her sexual orientation and the relationship secret had on her life. Similarly, there was an expectation that there would have been provided a fuller explanation about the reaction of her family when, as she claims, they found out about her sexual orientation following the May 2015 incident when, according to the applicant, she had already been the subject of harassment in the community for a few years.

[17] Finally, the RPD gave no weight to a letter provided by a Toronto organization, FrancoQueer. Basically, the letter recounts what the applicant has shared with the organization and, as such, is “self-reported information” to put it colloquially; the facts do not become better and more credible once reported by a third party if that person is reporting the information heard from the applicant. In a word, it is not independent evidence. The letter cannot, therefore, support the applicant’s contention.
III. Standard of review [18] The only issue in this case is whether or not the story told by the applicant carries weight in view of the credibility assessment conducted by the RPD. The parties are in agreement that the standard of review applicable in the circumstances is reasonableness. Indeed, the case law in this Court has been consistent to that effect (Manege v Canada (Citizenship and Immigration), 2014 FC 374 at para 14; Ramirez Martin v Canada (Citizenship and Immigration), 2010 FC 664 at para 11; Shukriya v Canada (Citizenship and Immigration), 2016 FC 1375 at para 11).

[19] It follows that this Court must be deferential towards the findings made by the RPD. If the outcome reached by the RPD falls within a range of possible, acceptable outcomes in view of the facts and the law, the decision must not be disturbed. Similarly, reasonableness is found where there is the existence of justification, transparency and intelligibility within the decision making process (Dunsmuir v New Brunswick, 2008 SCC 9, [2008] 1 SCR 190).
IV. Analysis [20] The assessment of credibility is based on life experience. There is no denying that the RPD has a special expertise in assessing the cases that present themselves before it. In their treatise, The Law of Evidence, 7th ed (Toronto: Irwin law, 2015), the authors David Paciocco and Lee Stuesser state:
In general, the trier of fact is entitled simply to apply common sense and human experience in determining whether evidence is credible and in deciding what use, if any, to make of it in coming to its finding of fact.

[21] Recently, Justice Tremblay-Lamer made a similar observation in Haramicheal v Canada (Citizenship and Immigration), 2016 FC 1197:

[15] The principles governing the assessment of an applicant’s credibility in the refugee context are well-established within this Court. The RAD is entitled to make findings of credibility based on implausibility, common sense and rationality (Lubana v Canada (Minister of Citizenship and Immigration), 2003 FCT 116). Adverse credibility findings should however not be based on a microscopic evaluation of issues peripheral or irrelevant to the case (Attakora v Canada (Minister of Employment and Immigration), [1989] FCJ No 444).
In effect, the RPD has to consider the entirety of the evidence. However, where most of the evidence comes from one deponent, if that witness is not believed, it is obviously probable that an applicant will not satisfy her burden to convince that she is a refugee or a person in need of protection. The burden is not insignificant as she must show, on a balance of probabilities, that the decision maker has made findings on credibility that are unreasonable.

[22] Very helpfully, Justice Henry Brown provided a summary of authorities on the assessment of credibility in Gong v Canada (Citizenship and Immigration), 2017 FC 165:

[9] Additional authorities on the assessment of credibility and plausibility are summarized as follows. First, the RPD has broad discretion to prefer certain evidence over other evidence and to determine the weight to be assigned to the evidence it accepts: Medarovik v Canada (Minister of Citizenship and Immigration), 2002 FCT 61 at para 16, Tremblay-Lamer, J; Pushpanathan v Canada (Minister of Citizenship and Immigration), 2002 FCT 867 at para 68, Blais J. Second, the Federal Court of Appeal confirms that findings of fact and determinations of credibility fall within the heartland of the expertise of the RPD: Giron v Canada (Minister of Employment and Immigration) (1992), 143 NR 238 (FCA) [Giron]. Third, the RPD is recognized to have expertise in assessing refugee claims and is authorized by statute to apply its specialized knowledge: Chen v Canada (Minister of Citizenship and Immigration), 2003 FCT 805 at para 10, O’Reilly, J; and see Siad v Canada (Secretary of State), [1997] 1 FC 608 at para 24 (FCA), where the Federal Court of Appeal said that the RPD, “… is uniquely situated to assess the credibility of a refugee claimant; credibility determinations, which lie within “the heartland of the discretion of triers of fact”, are entitled to considerable deference upon judicial review and cannot be overturned unless they are perverse, capricious or made without regard to the evidence. Third, it is well-established that the RPD may make credibility findings based on implausibility, common sense and rationality, although adverse credibility findings “should not be based on a microscopic evaluation of issues peripheral or irrelevant to the case”: Haramichael v Canada (Minister of Citizenship and Immigration), 2016 FC 1197 at para 15, Tremblay-Lamer J, citing Lubana v Canada (Minister of Citizenship and Immigration), 2003 FCT 116 at paras 10-11, Martineau J [Lubana]; Attakora v Canada (Minister of Employment and Immigration), [1989] FCJ No 444 (FCA). Fourth, the RPD may reject uncontradicted evidence if it “is not consistent with the probabilities affecting the case as a whole, or where inconsistencies are found in the evidence”: Lubana, above at para 10. Fifth, the RPD is entitled to conclude that an applicant is not credible “because of implausibilities in his or her evidence as long as its inferences are not unreasonable and its reasons are set out in ‘clear and unmistakable terms’”: Lubana, above at para 9.
[my emphasis]

[23] In spite of the valiant effort of counsel on behalf of the applicant, the Court must find that the RPD’s decision is reasonable. As indicated before, it does not suffice to claim that the RPD may have erred; what needs to be shown is that the outcome reached is either not justified, transparent, or intelligible, or it is not one of the possible, acceptable outcomes. I have read carefully the transcript of the testimony given by the applicant before the RPD and come to the conclusion that the outcome falls within the range of acceptable, possible outcomes and the decision has been amply justified.

[24] It was open for the RPD to consider the narrative as being implausible and the applicant less than credible when the evidence is examined in its entirety. The applicant is minimalist when presenting the relationship that forced her to leave her country of nationality for fear of violence. The only clear incident of violence is not described in any details either; while a brother and a sister were supposedly present, the applicant, who acknowledges in her testimony that she could have asked for their support to gain refugee status in Canada, did not receive any assistance.

[25] The applicant’s partner purportedly sends a letter, but it is type-written and bears a signature that may be seen as somewhat odd. The RPD noted the discrepancies between some aspects of the letter and the applicant’s testimony, in spite of its lack of details.

[26] While the applicant borrows money to attend an internship in Miami, Florida, which would allow her to escape her fear of death in Haiti, she returns to Haiti because her passport was kept by the organizers during the internship and she does not speak English. That, in and of itself, is surprising. But it is even more surprising that the applicant finds the financial resources to go again to the United States barely a month later, crosses the State of New York in its entirety to arrive at Fort Erie and then crosses the border into Canada, in Southern Ontario where her lack of proficiency in English would continue to be problematic.

[27] Counsel for the applicant has skillfully attempted to parse the questions and answers during the RPD hearing to disagree with the findings of credibility. In so doing, counsel conducted the same kind of microscopic evaluation of issues that is often complained about when done by administrative tribunals. In my view, this amounts to a disagreement on some of the findings made without showing that those findings are outside of the range of possible, acceptable outcomes. Indeed, it is the entirety of the evidence available on this record that must be assessed, applying common sense and human experience. I saw no perverse or capricious credibility determination which lies within the heartland of the discretion of triers of fact. That does not suggest that every time the RPD concludes on a matter of credibility that the conclusion becomes reasonable. It simply means that a tribunal, whose expertise is in assessing refugee claims, and where the credibility of the claimant is at the heart of the matter, deserves a healthy serving of deference upon judicial review.

[28] In the case at bar, I find that there was considerable evidence to support the findings. Contrary to what was argued, the reasons provide ample justification, transparency and intelligibility within the decision-making process.

[29] As a result, the judicial review application must be dismissed. There is no certified question.


## 9411:2 · paragraphs 28-29

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `5386c94e9b6851747e30f581714345326b3a7ba00ddb3034c272eba7d4bbf03e`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 9411:2:subtheme:1 · paragraphs 28-29

- Raw key terms: `imm-112-17, application, cause, certified, citizenship, court, date, dismissed`
- Display key terms: `imm-112-17, certified, date, dismissed`
- Argument roles: `disposition, issue`
- Explanation: Observed roles: disposition, issue Display terms: imm-112-17, certified, date, dismissed Operative outcome context: JUDGMENT in IMM-112-17 THIS COURT’S JUDGMENT is that the judicial review application is dismissed. Evidence spans paragraphs 28-29. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4476048` offsets `203-211`; context: No question is certified.
- Evidence: `disposition` cue `dismissed` at chunk `4476048` offsets `189-198`; context: JUDGMENT in IMM-112-17
THIS COURT’S JUDGMENT is that the judicial review application is dismissed.

#### Section text

JUDGMENT in IMM-112-17
THIS COURT’S JUDGMENT is that the judicial review application is dismissed. No question is certified.
"Yvan Roy"
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET:
IMM-112-17
STYLE OF CAUSE:
MARIE NERLANDE EDMOND v MINISTER OF CITIZENSHIP AND IMMIGRATION
PLACE OF HEARING:
Toronto, Ontario
DATE OF HEARING:
June 21, 2017


## 9411:3 · paragraphs 30-30

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `52c744eaafb7d5ce6348ac2593742b6eca723dd6b4e2aff6ca80b2d4c8dc317e`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 9411:3:subtheme:1 · paragraphs 30-30

- Raw key terms: `appearances, applicant, attorney, barrister, canada, dated, deputy, general`
- Display key terms: `barrister, dated, deputy`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: barrister, dated, deputy No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 30-30. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT AND REASONS
ROY J.
DATED:
July 4, 2017
APPEARANCES:
Richard Wazana
For The Applicant
Melissa Mathieu
For The Respondent
SOLICITORS OF RECORD:
Wazana Law
Barrister & Solicitor
Toronto, Ontario
For The Applicant
William F. Pentney
Deputy Attorney General of Canada
Toronto, Ontario
For The Respondent
