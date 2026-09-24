# Discussion Units: case 5465

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **43**
- Continuity pairs: **42**
- Discussion Units: **3**
- Paragraph source hashes: **43**
- Sub-themes: **13**

## 5465:1 · paragraphs 0-39

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `4810d21170bbfc6d583be78b63756551b94a65b5ce3bcfa02f3175d31e39000c`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 5465:1:subtheme:1 · paragraphs 0-3

- Raw key terms: `applicant, immigration, sadeghi-pari, board, canada, convention, decision, fariba`
- Display key terms: `sadeghi-pari, convention, fariba`
- Argument roles: `evidence_fact, governing_rule, party_position`
- Explanation: Observed roles: evidence_fact, governing_rule, party_position Display terms: sadeghi-pari, convention, fariba Position/evidence statements: She claimed Convention refugee status in Canada by reason of her fear of persecution due to her membership in a particular social group, namely, as a lesbian in Iran. | The applicant claims that she entered into a lesbian relationship with her friend, Farideh, beginning in her second last year of high school. Rule/authority context: She also claimed to be a person in need of protection, pursuant to the grounds set out in section 97 of the Immigration and Refugee Protection Act, S. Evidence spans paragraphs 0-3. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `determined that` at chunk `4301074` offsets `223-238`; context: In that decision, the Board determined that the applicant was not a Convention refugee or a person in need of protection.
- Evidence: `party_position` cue `claimed` at chunk `4301075` offsets `47-54`; context: She claimed Convention refugee status in Canada by reason of her fear of persecution due to her membership in a particular social group, namely, as a lesbian in Iran.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4301075` offsets `265-276`; context: She also claimed to be a person in need of protection, pursuant to the grounds set out in section 97 of the Immigration and Refugee Protection Act, S.
- Evidence: `party_position` cue `claims` at chunk `4301076` offsets `114-120`; context: The applicant claims that she entered into a lesbian relationship with her friend, Farideh, beginning in her second last year of high school.

#### 5465:1:subtheme:2 · paragraphs 4-14

- Raw key terms: `applicant, farideh, apartment, family, relationship, testified, told, call`
- Display key terms: `farideh, apartment, family, relationship, testified, told, call`
- Argument roles: `counterargument_limitation, evidence_fact, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, party_position, reasoning_application Display terms: farideh, apartment, family, relationship, testified, told, call Position/evidence statements: The applicant claims that her parents were quite upset and this strained their relationship for a number of months. | The applicant claims that she had to leave home and find her own apartment to rent. Application context: [4] In 1987, Farideh had problems with her family, therefore she moved out of the family home and rented an apartment in the Narmak district of Tehran. | [10] When Farideh was released, she had nowhere else to live therefore she went to live with the applicant. Evidence spans paragraphs 4-14. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `reasoning_application` cue `therefore` at chunk `4301077` offsets `51-60`; context: [4] In 1987, Farideh had problems with her family, therefore she moved out of the family home and rented an apartment in the Narmak district of Tehran.
- Evidence: `evidence_fact` cue `testimony` at chunk `4301078` offsets `75-84`; context: [5] The applicant set out in her Personal Information Form ("PIF") and her testimony that she believes her family knew about her relationship with Farideh but were very much in denial and it was never discussed amongst her family.
- Evidence: `party_position` cue `claims` at chunk `4301079` offsets `264-270`; context: The applicant claims that her parents were quite upset and this strained their relationship for a number of months.
- Evidence: `party_position` cue `claims` at chunk `4301082` offsets `201-207`; context: The applicant claims that she had to leave home and find her own apartment to rent.
- Evidence: `reasoning_application` cue `therefore` at chunk `4301083` offsets `61-70`; context: [10] When Farideh was released, she had nowhere else to live therefore she went to live with the applicant.
- Evidence: `counterargument_limitation` cue `however` at chunk `4301083` offsets `181-188`; context: The applicant testified that she was fearful of what might happen again, however, none of their friends would take Farideh in and Farideh's parents certainly would not.
- Evidence: `party_position` cue `claimed` at chunk `4301085` offsets `204-211`; context: She claimed Convention refugee status a week later, on September 30, 2000.

#### 5465:1:subtheme:3 · paragraphs 15-16

- Raw key terms: `applicant, board, concluded, having, without, able, according, affection`
- Display key terms: `concluded, having, without, able, according, affection`
- Argument roles: `disposition, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, issue, reasoning_application Display terms: concluded, having, without, able, according, affection Rule/authority context: The Board based that conclusion on the following implausibility findings: - the applicant would not have had the freedom to live so independently as she had stated that her family was a religious family that followed the Application context: The Board based that conclusion on the following implausibility findings: - the applicant would not have had the freedom to live so independently as she had stated that her family was a religious family that followed the Operative outcome context: The Board based that conclusion on the following implausibility findings: - the applicant would not have had the freedom to live so independently as she had stated that her family was a religious family that followed the Evidence spans paragraphs 15-16. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4301088` offsets `2076-2083`; context: The Board based that conclusion on the following implausibility findings:
- the applicant would not have had the freedom to live so independently as she had stated that her family was a religious family that followed the traditions of Islam;
- after being released from police custody, it is implausible that the only consequence within her family was that her parents would not speak to her, as she would have likely been treated more harshly;
- her "traditional Iranian" father and family would not have allowed her to move out of the family home and get her own apartment a short time after being charged by the police of being a lesbian and after this point her freedom would have been severely restricted by her family;
- it is "inconceivable" that the applicant would be allowed to have Farideh move in with her, as her parents would have monitored her lifestyle and made sure that she would not have had "such a roommate" moving in with her;
- it is implausible that the applicant was able to maintain a strained relationship with her parents after refusing an arranged marriage in 1998;
- the applicant's explanation as to why her family did not treat her more harshly was plausible in Canada, but not plausible in Iran, in a "traditional Orthodox Muslim family";
- as an unmarried female, the applicant would not have been permitted to spend such a great amount of time away from the family home, and even if she had been permitted to visit Farideh, her parents would have had to condone her visits;
- the applicant's testimony about the behaviour of the landlord, entering the apartment without knowledge and discovering "incriminating evidence", is not plausible, as a male in Iran would "never, under any circumstances, enter the apartment of an unmarried woman unannounced, regardless of whether he had a key and regardless of whether he was the landlord", for he would likely have been arrested and treated much more harshly than the applicant for so doing;
- the applicant's frequent visits to Farideh and their behaviour together would not have raised the suspicion of the landlord and neighbours because documentary evidence indicated that women in Iran show affection more openly to each other than women do in Canada.
- Evidence: `evidence_fact` cue `testimony` at chunk `4301088` offsets `1802-1811`; context: The Board based that conclusion on the following implausibility findings:
- the applicant would not have had the freedom to live so independently as she had stated that her family was a religious family that followed the traditions of Islam;
- after being released from police custody, it is implausible that the only consequence within her family was that her parents would not speak to her, as she would have likely been treated more harshly;
- her "traditional Iranian" father and family would not have allowed her to move out of the family home and get her own apartment a short time after being charged by the police of being a lesbian and after this point her freedom would have been severely restricted by her family;
- it is "inconceivable" that the applicant would be allowed to have Farideh move in with her, as her parents would have monitored her lifestyle and made sure that she would not have had "such a roommate" moving in with her;
- it is implausible that the applicant was able to maintain a strained relationship with her parents after refusing an arranged marriage in 1998;
- the applicant's explanation as to why her family did not treat her more harshly was plausible in Canada, but not plausible in Iran, in a "traditional Orthodox Muslim family";
- as an unmarried female, the applicant would not have been permitted to spend such a great amount of time away from the family home, and even if she had been permitted to visit Farideh, her parents would have had to condone her visits;
- the applicant's testimony about the behaviour of the landlord, entering the apartment without knowledge and discovering "incriminating evidence", is not plausible, as a male in Iran would "never, under any circumstances, enter the apartment of an unmarried woman unannounced, regardless of whether he had a key and regardless of whether he was the landlord", for he would likely have been arrested and treated much more harshly than the applicant for so doing;
- the applicant's frequent visits to Farideh and their behaviour together would not have raised the suspicion of the landlord and neighbours because documentary evidence indicated that women in Iran show affection more openly to each other than women do in Canada.
- Evidence: `governing_rule` cue `under` at chunk `4301088` offsets `1982-1987`; context: The Board based that conclusion on the following implausibility findings:
- the applicant would not have had the freedom to live so independently as she had stated that her family was a religious family that followed the traditions of Islam;
- after being released from police custody, it is implausible that the only consequence within her family was that her parents would not speak to her, as she would have likely been treated more harshly;
- her "traditional Iranian" father and family would not have allowed her to move out of the family home and get her own apartment a short time after being charged by the police of being a lesbian and after this point her freedom would have been severely restricted by her family;
- it is "inconceivable" that the applicant would be allowed to have Farideh move in with her, as her parents would have monitored her lifestyle and made sure that she would not have had "such a roommate" moving in with her;
- it is implausible that the applicant was able to maintain a strained relationship with her parents after refusing an arranged marriage in 1998;
- the applicant's explanation as to why her family did not treat her more harshly was plausible in Canada, but not plausible in Iran, in a "traditional Orthodox Muslim family";
- as an unmarried female, the applicant would not have been permitted to spend such a great amount of time away from the family home, and even if she had been permitted to visit Farideh, her parents would have had to condone her visits;
- the applicant's testimony about the behaviour of the landlord, entering the apartment without knowledge and discovering "incriminating evidence", is not plausible, as a male in Iran would "never, under any circumstances, enter the apartment of an unmarried woman unannounced, regardless of whether he had a key and regardless of whether he was the landlord", for he would likely have been arrested and treated much more harshly than the applicant for so doing;
- the applicant's frequent visits to Farideh and their behaviour together would not have raised the suspicion of the landlord and neighbours because documentary evidence indicated that women in Iran show affection more openly to each other than women do in Canada.
- Evidence: `reasoning_application` cue `because` at chunk `4301088` offsets `2388-2395`; context: The Board based that conclusion on the following implausibility findings:
- the applicant would not have had the freedom to live so independently as she had stated that her family was a religious family that followed the traditions of Islam;
- after being released from police custody, it is implausible that the only consequence within her family was that her parents would not speak to her, as she would have likely been treated more harshly;
- her "traditional Iranian" father and family would not have allowed her to move out of the family home and get her own apartment a short time after being charged by the police of being a lesbian and after this point her freedom would have been severely restricted by her family;
- it is "inconceivable" that the applicant would be allowed to have Farideh move in with her, as her parents would have monitored her lifestyle and made sure that she would not have had "such a roommate" moving in with her;
- it is implausible that the applicant was able to maintain a strained relationship with her parents after refusing an arranged marriage in 1998;
- the applicant's explanation as to why her family did not treat her more harshly was plausible in Canada, but not plausible in Iran, in a "traditional Orthodox Muslim family";
- as an unmarried female, the applicant would not have been permitted to spend such a great amount of time away from the family home, and even if she had been permitted to visit Farideh, her parents would have had to condone her visits;
- the applicant's testimony about the behaviour of the landlord, entering the apartment without knowledge and discovering "incriminating evidence", is not plausible, as a male in Iran would "never, under any circumstances, enter the apartment of an unmarried woman unannounced, regardless of whether he had a key and regardless of whether he was the landlord", for he would likely have been arrested and treated much more harshly than the applicant for so doing;
- the applicant's frequent visits to Farideh and their behaviour together would not have raised the suspicion of the landlord and neighbours because documentary evidence indicated that women in Iran show affection more openly to each other than women do in Canada.
- Evidence: `disposition` cue `allowed` at chunk `4301088` offsets `781-788`; context: The Board based that conclusion on the following implausibility findings:
- the applicant would not have had the freedom to live so independently as she had stated that her family was a religious family that followed the traditions of Islam;
- after being released from police custody, it is implausible that the only consequence within her family was that her parents would not speak to her, as she would have likely been treated more harshly;
- her "traditional Iranian" father and family would not have allowed her to move out of the family home and get her own apartment a short time after being charged by the police of being a lesbian and after this point her freedom would have been severely restricted by her family;
- it is "inconceivable" that the applicant would be allowed to have Farideh move in with her, as her parents would have monitored her lifestyle and made sure that she would not have had "such a roommate" moving in with her;
- it is implausible that the applicant was able to maintain a strained relationship with her parents after refusing an arranged marriage in 1998;
- the applicant's explanation as to why her family did not treat her more harshly was plausible in Canada, but not plausible in Iran, in a "traditional Orthodox Muslim family";
- as an unmarried female, the applicant would not have been permitted to spend such a great amount of time away from the family home, and even if she had been permitted to visit Farideh, her parents would have had to condone her visits;
- the applicant's testimony about the behaviour of the landlord, entering the apartment without knowledge and discovering "incriminating evidence", is not plausible, as a male in Iran would "never, under any circumstances, enter the apartment of an unmarried woman unannounced, regardless of whether he had a key and regardless of whether he was the landlord", for he would likely have been arrested and treated much more harshly than the applicant for so doing;
- the applicant's frequent visits to Farideh and their behaviour together would not have raised the suspicion of the landlord and neighbours because documentary evidence indicated that women in Iran show affection more openly to each other than women do in Canada.

#### 5465:1:subtheme:4 · paragraphs 17-19

- Raw key terms: `applicant, board, without, applicant's, based, board's, capricious, decision`
- Display key terms: `without, applicant's, based, board's, capricious`
- Argument roles: `counterargument_limitation, evidence_fact, issue`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue Display terms: without, applicant's, based, board's, capricious Evidence spans paragraphs 17-19. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `ISSUES` at chunk `4301090` offsets `759-765`; context: ISSUES
- Evidence: `evidence_fact` cue `evidence` at chunk `4301090` offsets `219-227`; context: The Board based this conclusion on the fact that the applicant had not provided any corroborating evidence, such as pictures of her with Farideh or reliable evidence that she was active or volunteering in the gay and lesbian community in Toronto.
- Evidence: `counterargument_limitation` cue `however` at chunk `4301090` offsets `502-509`; context: The Board acknowledged that such latter evidence may have been self-serving and was not necessary to a claim such as the applicant's, however, "it could have been helpful in establishing her sexual preference".
- Evidence: `issue` cue `whether` at chunk `4301091` offsets `390-397`; context: Did the Board err in law in requiring a higher than necessary standard of proof for determining whether the applicant was a lesbian and if so, does this raise a reasonable apprehension of bias?
- Evidence: `evidence_fact` cue `evidence` at chunk `4301092` offsets `410-418`; context: The respondent repeats the Board's reasoning in his factum, referring to the strict cultural and religious norms that exist in Iran, however, this suffers from the same flaw as the Board's reasoning, it is not supported by any documentary evidence on the tribunal record.
- Evidence: `counterargument_limitation` cue `however` at chunk `4301092` offsets `304-311`; context: The respondent repeats the Board's reasoning in his factum, referring to the strict cultural and religious norms that exist in Iran, however, this suffers from the same flaw as the Board's reasoning, it is not supported by any documentary evidence on the tribunal record.

#### 5465:1:subtheme:5 · paragraphs 20-21

- Raw key terms: `applicant, board, employment, allegations, already, applicant's, bring, canada`
- Display key terms: `employment, allegations, already, applicant's, bring`
- Argument roles: `evidence_fact, governing_rule, party_position`
- Explanation: Observed roles: evidence_fact, governing_rule, party_position Display terms: employment, allegations, already, applicant's, bring Position/evidence statements: Such possible difference are that life for women is different and less restrictive in the capital Tehran, than it is in smaller cities and the countryside, that the applicant had been engaged in full-time employment sinc Rule/authority context: Pursuant to the principle set out in Maldonado v. Evidence spans paragraphs 20-21. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `party_position` cue `claimed` at chunk `4301093` offsets `554-561`; context: Such possible difference are that life for women is different and less restrictive in the capital Tehran, than it is in smaller cities and the countryside, that the applicant had been engaged in full-time employment since 1987, first as a clothing designer and then as a secretary, giving her income and greater freedom than women who do not work and the applicant never claimed that her family was ultra-traditional.
- Evidence: `evidence_fact` cue `evidence` at chunk `4301094` offsets `78-86`; context: [21] The respondent is correct in stating that the applicant must bring forth evidence in support of her claim, however, it is well established that an applicant's testimony is regarded as such evidence.
- Evidence: `governing_rule` cue `Pursuant to` at chunk `4301094` offsets `204-215`; context: Pursuant to the principle set out in Maldonado v.

#### 5465:1:subtheme:6 · paragraphs 22-28

- Raw key terms: `board, applicant, findings, board's, evidence, opinion, plausibility, chance`
- Display key terms: `findings, board's, opinion, plausibility, chance`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position, reasoning_application Display terms: findings, board's, opinion, plausibility, chance Position/evidence statements: [28] The applicant has also argued that the Board erred in concluding that the applicant would not face a well-founded fear of persecution as she would only need to keep her relationship with another woman secret in orde Application context: I agree with the applicant that several of the Board's plausibility findings appear highly speculative, without grounding in any evidence, and are therefore, patently unreasonable: Arumugam, supra, Frimpong, supra. Evidence spans paragraphs 22-28. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4301095` offsets `75-83`; context: [22] The documentary evidence that the Board relied on deals only with the question of homosexuality and lesbianism in Iran, and does not deal with broader cultural attitudes towards employed, single women living in the capital, Tehran.
- Evidence: `evidence_fact` cue `evidence` at chunk `4301095` offsets `21-29`; context: [22] The documentary evidence that the Board relied on deals only with the question of homosexuality and lesbianism in Iran, and does not deal with broader cultural attitudes towards employed, single women living in the capital, Tehran.
- Evidence: `reasoning_application` cue `therefore` at chunk `4301095` offsets `384-393`; context: I agree with the applicant that several of the Board's plausibility findings appear highly speculative, without grounding in any evidence, and are therefore, patently unreasonable: Arumugam, supra, Frimpong, supra.
- Evidence: `evidence_fact` cue `evidence` at chunk `4301096` offsets `889-897`; context: Before using any information or opinion that is within its specialized knowledge, the Division must notify the claimant or protected person, and the Minister if the Minister is present at the hearing, and give them a chance to
(a) make representations on the reliability and use of the information or opinion; and
(b) give evidence in support of their representations.
- Evidence: `evidence_fact` cue `testimony` at chunk `4301097` offsets `153-162`; context: [24] I agree with the respondent that the Board may rely on its general expertise on country conditions in evaluating the plausibility of an applicant's testimony, and that documentary evidence on the standardized country file that is not specifically relied upon by the Board does not necessarily need to be reproduced on the tribunal record: Hassan, supra.
- Evidence: `counterargument_limitation` cue `However` at chunk `4301097` offsets `359-366`; context: However, this power of the Board is not open-ended to the extent that the Board can rely on numerous and specific observations about a country, without referring to some documentary evidence to supports its opinions.
- Evidence: `counterargument_limitation` cue `However` at chunk `4301099` offsets `209-216`; context: However, in other areas where the member later relied on specialized knowledge in its reasons to make implausibility findings, no such opportunity was given.
- Evidence: `evidence_fact` cue `testimony` at chunk `4301100` offsets `175-184`; context: [27] Another error in this case, is that the Board based its reasoning on the assumption that the applicant's family was a very strict, traditional Muslim family, whereas her testimony does not accord with this description.
- Evidence: `counterargument_limitation` cue `However` at chunk `4301100` offsets `454-461`; context: However, at page 3 of the Board's reasons, these answers are modified to mean that the applicant came from a "traditional Orthodox Muslim family" and a family that was "so traditional" that she could not have lived such a non-traditional lifestyle.
- Evidence: `party_position` cue `argued` at chunk `4301101` offsets `28-34`; context: [28] The applicant has also argued that the Board erred in concluding that the applicant would not face a well-founded fear of persecution as she would only need to keep her relationship with another woman secret in order to avoid punishment, as the documentary evidence indicated that once a lesbian relationship became public, the state would no longer be passive and would deal harshly with those accused of being in such a relationship.
- Evidence: `evidence_fact` cue `evidence` at chunk `4301101` offsets `262-270`; context: [28] The applicant has also argued that the Board erred in concluding that the applicant would not face a well-founded fear of persecution as she would only need to keep her relationship with another woman secret in order to avoid punishment, as the documentary evidence indicated that once a lesbian relationship became public, the state would no longer be passive and would deal harshly with those accused of being in such a relationship.

#### 5465:1:subtheme:7 · paragraphs 29-30

- Raw key terms: `issue, relationship, therefore, another, appears, application, attorney, authorities`
- Display key terms: `relationship, therefore, another, appears, authorities`
- Argument roles: `evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, reasoning_application Display terms: relationship, therefore, another, appears, authorities Application context: Concluding that persecution would not exist because a gay woman in Iran could live without punishment by hiding her relationship to another woman may be erroneous, as expecting an individual to live in such a manner coul | Therefore, this issue is not dispositive of this application for judicial review. Evidence spans paragraphs 29-30. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4301102` offsets `817-822`; context: ), dealing with the issue of claimants not being permitted to display their religious beliefs in public.
- Evidence: `reasoning_application` cue `because` at chunk `4301102` offsets `328-335`; context: Concluding that persecution would not exist because a gay woman in Iran could live without punishment by hiding her relationship to another woman may be erroneous, as expecting an individual to live in such a manner could be a serious interference with a basic human right, and therefore persecution.
- Evidence: `issue` cue `issue` at chunk `4301103` offsets `484-489`; context: Therefore, this issue is not dispositive of this application for judicial review.
- Evidence: `evidence_fact` cue `evidence` at chunk `4301103` offsets `132-140`; context: [30] However, in my view, while the Board appears to have started down the path towards this conclusion by referring to documentary evidence which indicates that lesbians are not sought after by the Iranian authorities as long as they keep their relationship in the private domain, this was not the basis for its rejection of her claim.
- Evidence: `reasoning_application` cue `Therefore` at chunk `4301103` offsets `468-477`; context: Therefore, this issue is not dispositive of this application for judicial review.

#### 5465:1:subtheme:8 · paragraphs 31-32

- Raw key terms: `authenticity, board, copy, document, fact, given, iran, member`
- Display key terms: `authenticity, copy, document, fact, given, iran`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: authenticity, copy, document, fact, given, iran Evidence spans paragraphs 31-32. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4301104` offsets `26-31`; context: [31] Moving to the second issue, namely the Board's view of the Iranian court summons document, I disagree with the respondent's contention that the Board made no finding as to the authenticity of this document.

#### 5465:1:subtheme:9 · paragraphs 33-35

- Raw key terms: `board, applicant, counsel, document, member, original, adducing, appears`
- Display key terms: `document, original, adducing, appears`
- Argument roles: `evidence_fact, issue, party_position`
- Explanation: Observed roles: evidence_fact, issue, party_position Display terms: document, original, adducing, appears Position/evidence statements: [33] As appears from the transcript of the hearing, at page 147 of the tribunal record, the Board member began to question the applicant about this document, however, he was interrupted by counsel who attempted to clarif Evidence spans paragraphs 33-35. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4301106` offsets `114-122`; context: [33] As appears from the transcript of the hearing, at page 147 of the tribunal record, the Board member began to question the applicant about this document, however, he was interrupted by counsel who attempted to clarify the Board's previous question as to why the document was only submitted at the hearing, being that there was a delay in obtaining a translation of the document.
- Evidence: `party_position` cue `submitted` at chunk `4301106` offsets `284-293`; context: [33] As appears from the transcript of the hearing, at page 147 of the tribunal record, the Board member began to question the applicant about this document, however, he was interrupted by counsel who attempted to clarify the Board's previous question as to why the document was only submitted at the hearing, being that there was a delay in obtaining a translation of the document.
- Evidence: `evidence_fact` cue `record` at chunk `4301106` offsets `80-86`; context: [33] As appears from the transcript of the hearing, at page 147 of the tribunal record, the Board member began to question the applicant about this document, however, he was interrupted by counsel who attempted to clarify the Board's previous question as to why the document was only submitted at the hearing, being that there was a delay in obtaining a translation of the document.
- Evidence: `evidence_fact` cue `evidence` at chunk `4301108` offsets `260-268`; context: stated at paragraph 6:
In this instance, the Board challenged the validity of the birth certificate without adducing any evidence in support of its contention and, clearly, the matter of foreign documents is not an area where the Board can claim particular knowledge.

#### 5465:1:subtheme:10 · paragraphs 36-37

- Raw key terms: `applicant, board, document, evidence, alert, area, authenticity, authorize`
- Display key terms: `document, alert, area, authenticity, authorize`
- Argument roles: `evidence_fact, governing_rule, issue`
- Explanation: Observed roles: evidence_fact, governing_rule, issue Display terms: document, alert, area, authenticity, authorize Rule/authority context: This is not an area where the Board can claim to have specialized knowledge, within Rule 18 of the Refugee Protection Division Rules, and further, even if it was such an area, the applicant should have been notified purs Evidence spans paragraphs 36-37. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4301109` offsets `279-286`; context: The Board refers to no documentary evidence about the nature of documents issued by the courts or the state of Iran, or whether falsified documents are easily obtainable in Iran.
- Evidence: `evidence_fact` cue `record` at chunk `4301109` offsets `48-54`; context: [36] There is no indication, in my view, on the record that the Board member is an expert in the matter of evaluating the authenticity of documents from Iran.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4301109` offsets `554-565`; context: This is not an area where the Board can claim to have specialized knowledge, within Rule 18 of the Refugee Protection Division Rules, and further, even if it was such an area, the applicant should have been notified pursuant to that Rule, that the Board had doubts about the authenticity of the document.
- Evidence: `evidence_fact` cue `evidence` at chunk `4301110` offsets `283-291`; context: I declined to authorize filing in these circumstances as it would constitute new evidence not before the Board.

#### 5465:1:subtheme:11 · paragraphs 38-39

- Raw key terms: `board, reasons, standard, above, absent, adverse, applicant, applicant's`
- Display key terms: `standard, above, absent, adverse, applicant's`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: standard, above, absent, adverse, applicant's Application context: In such a situation, the Board would not apply an erroneously high standard of proof. Evidence spans paragraphs 38-39. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4301111` offsets `15-20`; context: [38] The third issue raised in this application is whether the Board erred in applying a higher standard of proof to the issue of the applicant's sexual orientation.
- Evidence: `evidence_fact` cue `testimony` at chunk `4301111` offsets `265-274`; context: The Board, for the reasons set out above, capriciously doubted the truthfulness of the applicant's testimony and found the applicant's testimony implausible.
- Evidence: `reasoning_application` cue `apply` at chunk `4301111` offsets `652-657`; context: In such a situation, the Board would not apply an erroneously high standard of proof.
- Evidence: `counterargument_limitation` cue `However` at chunk `4301111` offsets `324-331`; context: However, if such plausibility findings had been supported by evidence, then in my opinion, the Board would have been entitled to draw an adverse inference from the fact that the applicant had no pictures of herself and her partner or other evidence supporting her claim to be a lesbian.

#### Section text

Sadeghi-Pari v. Canada (Minister of Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2004-02-26
Neutral citation
2004 FC 282
File numbers
IMM-1595-03
Decision Content
Date: 20040226
Docket: IMM-1595-03
Citation: 2004 FC 282
Toronto, Ontario, February 26th, 2004
Present: The Honourable Mr. Justice Mosley
BETWEEN:
FARIBA SADEGHI-PARI
Applicant
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
REASONS FOR ORDER AND ORDER

[1] The applicant, Ms. Fariba Sadeghi-Pari, seeks judicial review of the decision of the Refugee Protection Division, Immigration and Refugee Board (the "Board"), reasons dated February 3, 2003. In that decision, the Board determined that the applicant was not a Convention refugee or a person in need of protection. The applicant requests an order setting aside the Board's decision and an order that a different Board reconsider her claim.
BACKGROUND

[2] Ms. Sadeghi-Pari is a citizen of Iran. She claimed Convention refugee status in Canada by reason of her fear of persecution due to her membership in a particular social group, namely, as a lesbian in Iran. She also claimed to be a person in need of protection, pursuant to the grounds set out in section 97 of the Immigration and Refugee Protection Act, S.C. 2001, c. 27 ("IRPA").

[3] The applicant is from Tehran. At the time of her hearing before the Board she was 34 years old. The applicant claims that she entered into a lesbian relationship with her friend, Farideh, beginning in her second last year of high school. After high school the applicant began working as a clothing designer.

[4] In 1987, Farideh had problems with her family, therefore she moved out of the family home and rented an apartment in the Narmak district of Tehran. The applicant helped in paying the rent for this apartment. The applicant testified that she would visit Farideh almost every day, from 5:00 pm until 9 or 10 in the evening. Occasionally, she stayed the night. She testified that it became clear to her and Farideh that the landlord and neighbours were suspicious of their relationship.

[5] The applicant set out in her Personal Information Form ("PIF") and her testimony that she believes her family knew about her relationship with Farideh but were very much in denial and it was never discussed amongst her family.

[6] In 1998, the applicant refused to be married to a relative who had proposed. She did not explain the true reason to her family, but simply told her parents that she was not ready for marriage and that when she was, she would find her own person. The applicant claims that her parents were quite upset and this strained their relationship for a number of months. Farideh and the applicant continued their relationship.

[7] In December 1999, the applicant received a call from Farideh telling her that Farideh's landlord had gone into her apartment without permission and found pictures, books and other items which indicated that they were in a lesbian relationship. Farideh told the applicant not to come to her apartment that day.

[8] The applicant went to Farideh's apartment the next day and saw the landlord. He told her that he had called the police. Two members of the "religious police" soon arrived at Farideh's building and the applicant was arrested, taken to the police station and told that she would be charged with sexual crimes and punished by receiving 100 lashes. The applicant was permitted to call her father and he was able to pay a bribe to have her released from custody. The applicant later learned that Farideh had also been arrested and was not released until mid-January 2000.

[9] The applicant testified that after she returned home no one in her family would speak to her and that her father stated that this was the worst thing that could happen to his family. The applicant claims that she had to leave home and find her own apartment to rent. She did this sometime soon after her release, in December 1999 or early January 2000.

[10] When Farideh was released, she had nowhere else to live therefore she went to live with the applicant. The applicant testified that she was fearful of what might happen again, however, none of their friends would take Farideh in and Farideh's parents certainly would not.

[11] On March 21, 2000 the applicant went to visit her family for the Iranian New Years celebration. While there she received a phone call telling her that the religious police had raided her apartment and arrested Farideh. As a result, the applicant, with the help of her family, went into hiding and left Iran for Turkey on August 9, 2000.

[12] A smuggler took her by car to Turkey where she stayed for six weeks until arrangements were made for her to travel to Canada. She arrived in Canada, via the United States, on September 22, 2000. She claimed Convention refugee status a week later, on September 30, 2000.

[13] At the hearing, the applicant testified that she had heard word about Farideh, through her sister, and was told that she spent six to seven months in prison, and was badly treated there. The applicant believes that Farideh attempted to leave Iran for Turkey but at the time of the hearing she had not heard from her for approximately five months.

[14] The applicant's hearing before the Board was held on January 21, 2003. The Board rejected the applicant's claim in reasons dated February 3, 2003.
The Board's Decision

[15] The Board concluded that on a balance of probabilities the applicant's claim that she had been arrested for having a lesbian relationship and that the police, after her release, raided her apartment looking for her, and arrested her partner, Farideh, was not plausible. The Board based that conclusion on the following implausibility findings:
- the applicant would not have had the freedom to live so independently as she had stated that her family was a religious family that followed the traditions of Islam;
- after being released from police custody, it is implausible that the only consequence within her family was that her parents would not speak to her, as she would have likely been treated more harshly;
- her "traditional Iranian" father and family would not have allowed her to move out of the family home and get her own apartment a short time after being charged by the police of being a lesbian and after this point her freedom would have been severely restricted by her family;
- it is "inconceivable" that the applicant would be allowed to have Farideh move in with her, as her parents would have monitored her lifestyle and made sure that she would not have had "such a roommate" moving in with her;
- it is implausible that the applicant was able to maintain a strained relationship with her parents after refusing an arranged marriage in 1998;
- the applicant's explanation as to why her family did not treat her more harshly was plausible in Canada, but not plausible in Iran, in a "traditional Orthodox Muslim family";
- as an unmarried female, the applicant would not have been permitted to spend such a great amount of time away from the family home, and even if she had been permitted to visit Farideh, her parents would have had to condone her visits;
- the applicant's testimony about the behaviour of the landlord, entering the apartment without knowledge and discovering "incriminating evidence", is not plausible, as a male in Iran would "never, under any circumstances, enter the apartment of an unmarried woman unannounced, regardless of whether he had a key and regardless of whether he was the landlord", for he would likely have been arrested and treated much more harshly than the applicant for so doing;
- the applicant's frequent visits to Farideh and their behaviour together would not have raised the suspicion of the landlord and neighbours because documentary evidence indicated that women in Iran show affection more openly to each other than women do in Canada.

[16] The Board also concluded that a document tendered by the applicant, a summons from the Tehran Islamic Revolutionary Court was possibly forged, and assigned it little weight. The Board noted that the original copy of this document was on plain white paper, and despite having a stamp at the bottom, "the document itself looked to be a copy" and according to the Board, "given modern technology, this document could have been easily reproduced without any difficulty."

[17] Finally, the Board stated that it did not believe, on a balance of probabilities, that the applicant was a lesbian. The Board based this conclusion on the fact that the applicant had not provided any corroborating evidence, such as pictures of her with Farideh or reliable evidence that she was active or volunteering in the gay and lesbian community in Toronto. The Board acknowledged that such latter evidence may have been self-serving and was not necessary to a claim such as the applicant's, however, "it could have been helpful in establishing her sexual preference". The Board also found that the fact that she is unmarried and 34-years old does not necessarily indicate that she is a lesbian and she may be married without the Board's knowledge.
ISSUES

[18] 1. Did the Board base its decision on erroneous findings of fact, made in a perverse or capricious manner or without regard for the material before it, and in particular did the Board rely on generalizations?
2. Did the Board err in dismissing the authenticity of the summons document?
3. Did the Board err in law in requiring a higher than necessary standard of proof for determining whether the applicant was a lesbian and if so, does this raise a reasonable apprehension of bias?
ANALYSIS

[19] In my opinion, the applicant has demonstrated that the Board based its decision on several implausibility findings that were made in a perverse or capricious manner. The respondent repeats the Board's reasoning in his factum, referring to the strict cultural and religious norms that exist in Iran, however, this suffers from the same flaw as the Board's reasoning, it is not supported by any documentary evidence on the tribunal record. Further, it presents a monolithic view of Islamic and Iranian culture, without taking into account possible differences between the applicant's situation and the generalized norm.

[20] The Board ignored characteristics about the applicant that indicated that her situation may not be similar to situations of other Iranian women already encountered by the Board. Such possible difference are that life for women is different and less restrictive in the capital Tehran, than it is in smaller cities and the countryside, that the applicant had been engaged in full-time employment since 1987, first as a clothing designer and then as a secretary, giving her income and greater freedom than women who do not work and the applicant never claimed that her family was ultra-traditional.

[21] The respondent is correct in stating that the applicant must bring forth evidence in support of her claim, however, it is well established that an applicant's testimony is regarded as such evidence. Pursuant to the principle set out in Maldonado v. Canada (Minister of Employment and Immigration), [1980] 2 F.C. 302 (C.A.), when an applicant swears to the truth of certain allegations, this creates a presumption that those allegations are true unless there is a valid reason to doubt their truthfulness. In light of the applicant's clear, non-evasive and consistent testimony, with which the Board did not find fault in terms of demeanour, internal contradictions or inconsistencies, the Board erred in failing to set out evidence which rebutted the Maldonado, supra, presumption of truthfulness in the applicant's testimony.

[22] The documentary evidence that the Board relied on deals only with the question of homosexuality and lesbianism in Iran, and does not deal with broader cultural attitudes towards employed, single women living in the capital, Tehran. I agree with the applicant that several of the Board's plausibility findings appear highly speculative, without grounding in any evidence, and are therefore, patently unreasonable: Arumugam, supra, Frimpong, supra.

[23] The respondent maintains that the Board was entitled to take notice of facts and information within its specialized knowledge and for this reason its plausibility findings were reasonably open to it. Section 170(I) of IRPA and Rule 18 of the Refugee Protection Division Rules, SOR/2002-228, set out as follows:
170. The Refugee Protection Division, in any proceeding before it,
...
(I) may take notice of any facts that may be judicially noticed, any other generally recognized facts and any information or opinion that is within its specialized knowledge.
18. Before using any information or opinion that is within its specialized knowledge, the Division must notify the claimant or protected person, and the Minister if the Minister is present at the hearing, and give them a chance to
(a) make representations on the reliability and use of the information or opinion; and
(b) give evidence in support of their representations.
170. Dans toute affaire don't elle est saisie, la Section de la protection des réfugiés :
...
I) peut admettre d'office les faits admissibles en justice et les faits généralement reconnus et les renseignements ou opinions qui sont du ressort de sa spécialisation.
18. Avant d'utiliser un renseignement ou une opinion qui est du ressort de sa spécialisation, la Section en avise le demandeur d'asile ou la personne protégée et le ministre -- si celui-ci est présent à l'audience -- et leur donne la possibilité de :
a) faire des observations sur la fiabilité et l'utilisation du renseignement ou de l'opinion;
b) fournir des éléments de preuve à l'appui de leurs observations.

[24] I agree with the respondent that the Board may rely on its general expertise on country conditions in evaluating the plausibility of an applicant's testimony, and that documentary evidence on the standardized country file that is not specifically relied upon by the Board does not necessarily need to be reproduced on the tribunal record: Hassan, supra. However, this power of the Board is not open-ended to the extent that the Board can rely on numerous and specific observations about a country, without referring to some documentary evidence to supports its opinions. In this case, in my opinion, the Board relied on several, specific observations about life in Tehran, without referring to any sociological, human rights or other country evidence in support of its conclusions. As noted the only documentary evidence referred to in the Board's reasons relates to the prevalence and punishment for lesbianism and homosexuality in Iran, and does not address the Board's findings in relation to the freedom of unmarried women in Tehran.

[25] Moreover, even if the Board's opinions are viewed as being within its "specialized knowledge", then the applicant should have been given a chance to make representations on these opinions at the hearing.

[26] The transcript shows that the Board member, in some areas, did signal to the applicant his opinion about how it was not his experience that a single woman would be able to have her own apartment in Iran. However, in other areas where the member later relied on specialized knowledge in its reasons to make implausibility findings, no such opportunity was given. For example, the Board did not give the applicant a chance to respond to his opinion that a landlord who entered an unmarried woman's apartment would be treated more harshly than occupants who were found to be lesbians and why as an unmarried woman was she permitted to spend so much time away from the family home.

[27] Another error in this case, is that the Board based its reasoning on the assumption that the applicant's family was a very strict, traditional Muslim family, whereas her testimony does not accord with this description. Upon comparison with the transcript of the hearing, the Board correctly recounts the applicant's testimony at page 2 of its reasons, that is, that she came from "religious family", and one that "followed the traditions of Islam". However, at page 3 of the Board's reasons, these answers are modified to mean that the applicant came from a "traditional Orthodox Muslim family" and a family that was "so traditional" that she could not have lived such a non-traditional lifestyle. The Board misconstrued the applicant's testimony, in my opinion, and based many of its plausibility findings on this misconception that the applicant was from a very religious and traditional family.

[28] The applicant has also argued that the Board erred in concluding that the applicant would not face a well-founded fear of persecution as she would only need to keep her relationship with another woman secret in order to avoid punishment, as the documentary evidence indicated that once a lesbian relationship became public, the state would no longer be passive and would deal harshly with those accused of being in such a relationship.

[29] The meaning of persecution, as set out in the seminal decisions of Canada (Attorney General) v. Ward, [1993] 2 S.C.R. 689 and Chan v. Canada (Minister of Employment and Immigration), [1995] 3 S.C.R. 593, is generally defined as the serious interference with a basic human right. Concluding that persecution would not exist because a gay woman in Iran could live without punishment by hiding her relationship to another woman may be erroneous, as expecting an individual to live in such a manner could be a serious interference with a basic human right, and therefore persecution. See for example, the decisions of Fosu v. Canada (Minister of Employment and Immigration) (1994), 90 F.T.R. 182, Husseini v. Canada (Minister of Citizenship and Immigration) (2002), 20 Imm. L.R. (3d) 92 (F.C.T.D.), dealing with the issue of claimants not being permitted to display their religious beliefs in public.

[30] However, in my view, while the Board appears to have started down the path towards this conclusion by referring to documentary evidence which indicates that lesbians are not sought after by the Iranian authorities as long as they keep their relationship in the private domain, this was not the basis for its rejection of her claim. The Board found rather that its implausibility findings supported its conclusion that she likely did not have such a relationship. Therefore, this issue is not dispositive of this application for judicial review.

[31] Moving to the second issue, namely the Board's view of the Iranian court summons document, I disagree with the respondent's contention that the Board made no finding as to the authenticity of this document. While the Board member did not use the word "forgery", he set out his problems with the appearance of the document and then stated that it could have been easily reproduced, given modern technology, which, in my opinion, amounts to finding it to be a false document. The Board stated its reasons for disbelieving its authenticity at pages 7-8 of its reasons as follows:
...The panel notes that this document was on a plain piece of white paper. The panel was able to examine the original document and notes that while it did have a stamp at the bottom, the document itself looked to be a copy. In the panel's opinion, given modern technology, this document could have been easily reproduced without any difficulty. Given this and given the fact that there is no envelope to even show that it comes from Iran, the panel gives it little weight.

[32] The applicant attests that the document she produced for the Board member was in fact a photocopy and that there is nothing strange about this fact, as the authorities in Iran keep the originals of such documents and give persons concerned a copy with a stamp on it to prove its genuineness. The applicant also attests that if the Board member doubted the authenticity of the document, then she shoul

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]


## 5465:2 · paragraphs 40-41

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `d917c2f59960bc29fcd2fdc734f1ede3303acd2c3be78d4c812a64212cd3f8b2`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 5465:2:subtheme:1 · paragraphs 40-41

- Raw key terms: `reasons, above, accordance, allowed, applicant's, application, aside, board`
- Display key terms: `above, accordance, allowed, applicant's, aside`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: above, accordance, allowed, applicant's, aside No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 40-41. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

ORDER
THIS COURT ORDERS that this application for judicial review is allowed, the decision of the Board is set aside and the applicant's claim to be a Convention refugee and a person in need of protection is remitted to a different panel of the Board for redetermination in accordance with these reasons. No question is certified.
"Richard G. Mosley"
J.F.C.
I HEREBY CERTIFY that the above document is a true copy of the original filed of record in the Registry of the Federal Court the __________ day of _____________ A.D. 2004
Dated this _______ day of _______________, 2004
_______________________________
Name, Title of Officer
FEDERAL COURT
NAMES OF COUNSEL AND SOLICITORS OF RECORD
DOCKET: IMM-1595-03

STYLE OF CAUSE: FARIBA SADEGHI-PARI
and
MCI
DATE OF HEARING: FEBRUARY 25, 2004
PLACE OF HEARING: TORONTO, ONTARIO
REASONS FOR 

## 5465:3 · paragraphs 42-42

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `c2108c2d98b07dd03c63b1484ab059c65a823452415bc8a55a5cd68d8dea09a5`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 5465:3:subtheme:1 · paragraphs 42-42

- Raw key terms: `appearances, applicant, attorney, canada, citizenship, court, date, dated`
- Display key terms: `date, dated`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: date, dated No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 42-42. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

ORDER
AND ORDER BY: MOSLEY J.
DATED: FEBRUARY 26, 2004
APPEARANCES BY:
Randal Montgomery For the Applicant
Mr. Marcel Larouche For the Respondent
SOLICITORS OF RECORD:
Randal Montgomery
Toronto, Ontario For the Applicant
Morris Rosenberg
Deputy Attorney General of Canada
Toronto, Ontario For the Respondent
FEDERAL COURT
TRIAL DIVISION
Date: 20040226
Docket: IMM-1595-03
BETWEEN:
FARIBA SADEGHI-PARI
Applicant
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
REASONS FOR ORDER
AND ORDER
