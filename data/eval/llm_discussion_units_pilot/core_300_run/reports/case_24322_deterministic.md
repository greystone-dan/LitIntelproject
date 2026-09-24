# Discussion Units: case 24322

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **50**
- Continuity pairs: **49**
- Discussion Units: **8**
- Paragraph source hashes: **50**
- Sub-themes: **15**

## 24322:1 · paragraphs 0-27

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `92b7af1dd5ecb3d6ea7a7bf99daa64bdff11d1bdded632f3e91fe0a4a067e847`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 24322:1:subtheme:1 · paragraphs 0-1

- Raw key terms: `applicant, decision, immigration, application, barinder, canada, citation, citizenship`
- Display key terms: `barinder, citation`
- Argument roles: `governing_rule`
- Explanation: Observed roles: governing_rule Display terms: barinder, citation Rule/authority context: [1] This is an application for judicial review under subsection 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [“IRPA”] of a decision of the Refugee Protection Division [“RPD”], dated December 21, 201 Evidence spans paragraphs 0-1. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `under` at chunk `5144038` offsets `47-52`; context: [1] This is an application for judicial review under subsection 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [“IRPA”] of a decision of the Refugee Protection Division [“RPD”], dated December 21, 2012 that the Applicant was neither a “Convention refugee” within the meaning of section 96 of the IRPA nor a “person in need of protection” under subsection 97(1) of the IRPA.

#### 24322:1:subtheme:2 · paragraphs 2-16

- Raw key terms: `applicant, father, irpa, italy, makhan, singh, canada, section`
- Display key terms: `father, irpa, italy, makhan, singh, section`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: father, irpa, italy, makhan, singh, section Position/evidence statements: He claims to be a “Convention refugee” and a “person in need of protection” within the meaning of section 96 and subsection 97(1) of the IRPA. | [10] The RPD was satisfied with the evidence submitted pertaining to the Applicant’s identity. Rule/authority context: The RPD however analyzed the claim solely under subsection 97(1) of the IRPA. | Decision under review Application context: The people who attacked him told him they did so because his father humiliated Makhan Singh by taking back the land. Operative outcome context: Having granted the motion, it was then suggested by counsel for the Respondent that I dismiss the judicial review. Evidence spans paragraphs 2-16. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5144039` offsets `683-688`; context: I suggested that it was in the interest of justice that I hear it in the absence of the Applicant since the Applicant is not reachable and that the submissions of his counsel are already part of the Applicant’s motion record and that the issue raised is limited to the internal flight alternative [“IFA”].
- Evidence: `evidence_fact` cue `record` at chunk `5144039` offsets `79-85`; context: [2] Counsel for the Applicant presented a motion to be removed as solicitor of record due to the facts that the Applicant is not reachable, that his phone has been cancelled and that it is known in the Punjabi community that he has left the country.
- Evidence: `disposition` cue `granted` at chunk `5144039` offsets `337-344`; context: Having granted the motion, it was then suggested by counsel for the Respondent that I dismiss the judicial review.
- Evidence: `party_position` cue `claims` at chunk `5144040` offsets `57-63`; context: He claims to be a “Convention refugee” and a “person in need of protection” within the meaning of section 96 and subsection 97(1) of the IRPA.
- Evidence: `governing_rule` cue `under` at chunk `5144040` offsets `239-244`; context: The RPD however analyzed the claim solely under subsection 97(1) of the IRPA.
- Evidence: `counterargument_limitation` cue `however` at chunk `5144040` offsets `205-212`; context: The RPD however analyzed the claim solely under subsection 97(1) of the IRPA.
- Evidence: `counterargument_limitation` cue `however` at chunk `5144042` offsets `140-147`; context: A few months later, however, Makhan Singh stopped paying rent.
- Evidence: `reasoning_application` cue `because` at chunk `5144043` offsets `149-156`; context: The people who attacked him told him they did so because his father humiliated Makhan Singh by taking back the land.
- Evidence: `governing_rule` cue `under` at chunk `5144046` offsets `143-148`; context: Decision under review
- Evidence: `party_position` cue `submitted` at chunk `5144047` offsets `45-54`; context: [10] The RPD was satisfied with the evidence submitted pertaining to the Applicant’s identity.
- Evidence: `evidence_fact` cue `evidence` at chunk `5144047` offsets `36-44`; context: [10] The RPD was satisfied with the evidence submitted pertaining to the Applicant’s identity.
- Evidence: `evidence_fact` cue `determined that` at chunk `5144048` offsets `13-28`; context: [11] The RPD determined that the Applicant is neither a Convention refugee nor a person in need of protection pursuant to section 96 and subsection 97(1) of the IRPA.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5144048` offsets `110-121`; context: [11] The RPD determined that the Applicant is neither a Convention refugee nor a person in need of protection pursuant to section 96 and subsection 97(1) of the IRPA.
- Evidence: `party_position` cue `submitted` at chunk `5144049` offsets `58-67`; context: [12] The RPD noted that according to documentary evidence submitted regarding the requirements for residence in
Italy
, a permanent resident who is absent from the country for 12 months or more loses permanent resident status.
- Evidence: `evidence_fact` cue `evidence` at chunk `5144049` offsets `49-57`; context: [12] The RPD noted that according to documentary evidence submitted regarding the requirements for residence in
Italy
, a permanent resident who is absent from the country for 12 months or more loses permanent resident status.
- Evidence: `governing_rule` cue `under` at chunk `5144050` offsets `55-60`; context: [13] The RPD examined the Applicant’s exclusion status under Article 1E of Article 1 of the Convention Against Torture and Other Cruel, Inhuman or Degrading Treatment or Punishment, and concluded that he was not excluded given that he had come to Canada as a minor and that the decision was not his, but his father’s.
- Evidence: `counterargument_limitation` cue `but` at chunk `5144050` offsets `300-303`; context: [13] The RPD examined the Applicant’s exclusion status under Article 1E of Article 1 of the Convention Against Torture and Other Cruel, Inhuman or Degrading Treatment or Punishment, and concluded that he was not excluded given that he had come to Canada as a minor and that the decision was not his, but his father’s.
- Evidence: `party_position` cue `claimed` at chunk `5144052` offsets `53-60`; context: [15] According to the RPD, even though the Applicant claimed that Makhan Singh is influential with police and politicians and that he uses the police to exact revenge on people, there wasn’t enough evidence that the police were intending to make any false case against the Applicant for any reason that would engage one of the grounds within section 96 of the IRPA.
- Evidence: `evidence_fact` cue `evidence` at chunk `5144052` offsets `198-206`; context: [15] According to the RPD, even though the Applicant claimed that Makhan Singh is influential with police and politicians and that he uses the police to exact revenge on people, there wasn’t enough evidence that the police were intending to make any false case against the Applicant for any reason that would engage one of the grounds within section 96 of the IRPA.
- Evidence: `governing_rule` cue `under` at chunk `5144053` offsets `53-58`; context: [16] Consequently, the RPD analyzed the claim solely under subsection 97(1) of the IRPA.

#### 24322:1:subtheme:3 · paragraphs 17-22

- Raw key terms: `applicant, concluded, bangalore, calcutta, delhi, evidence, life, likely`
- Display key terms: `concluded, bangalore, calcutta, delhi, life, likely`
- Argument roles: `evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, reasoning_application Display terms: concluded, bangalore, calcutta, delhi, life, likely Application context: The RPD found that the basis of that fear was speculative and that there was insufficient evidence to conclude that it was more probable than not that Makhan Singh’s influence extends to other states mentioned as possibl | Based on objective evidence, the RPD found that, while police inspections are made in various cities because of the obligation of landlords and employers to report newcomers, it was not more likely than not that the poli Evidence spans paragraphs 17-22. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5144054` offsets `42-47`; context: [17] The RPD noted that the determinative issue in the claim lay in the availability of an IFA and concluded to the existence of multiple IFAs, namely
New Delhi ,
Bangalore and
Calcutta
.
- Evidence: `evidence_fact` cue `found that` at chunk `5144055` offsets `526-536`; context: The RPD found that the basis of that fear was speculative and that there was insufficient evidence to conclude that it was more probable than not that Makhan Singh’s influence extends to other states mentioned as possible refuges.
- Evidence: `reasoning_application` cue `conclude` at chunk `5144055` offsets `620-628`; context: The RPD found that the basis of that fear was speculative and that there was insufficient evidence to conclude that it was more probable than not that Makhan Singh’s influence extends to other states mentioned as possible refuges.
- Evidence: `evidence_fact` cue `evidence` at chunk `5144056` offsets `274-282`; context: Based on objective evidence, the RPD found that, while police inspections are made in various cities because of the obligation of landlords and employers to report newcomers, it was not more likely than not that the police would bring forward a false accusation in the Applicant’s case.
- Evidence: `reasoning_application` cue `because` at chunk `5144056` offsets `356-363`; context: Based on objective evidence, the RPD found that, while police inspections are made in various cities because of the obligation of landlords and employers to report newcomers, it was not more likely than not that the police would bring forward a false accusation in the Applicant’s case.
- Evidence: `evidence_fact` cue `determined that` at chunk `5144058` offsets `25-40`; context: [21] Ultimately, the RPD determined that it was reasonable for the Applicant to relocate, as he is a young adult of 22 years of age and, given that in the Applicant’s circumstances, there is no evidence of hardship in relocating that would give rise to a risk to life or safety, as required by the reasonableness test for an IFA.

#### 24322:1:subtheme:4 · paragraphs 23-25

- Raw key terms: `applicant, erred, issue, submits, according, adds, amounted, argues`
- Display key terms: `erred, submits, according, adds, amounted, argues`
- Argument roles: `evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, party_position, reasoning_application Display terms: erred, submits, according, adds, amounted, argues Position/evidence statements: [23] The Applicant submits that the RPD erred in fact and in law in concluding that he could live safely in New Delhi , Bangalore or Calcutta . | [25] Contrary to the RPD’s finding pertaining to the Applicant’s knowledge of how far Makhan Singh’s influence extended, the Applicant argues that he did indeed testify and confirm that the man’s influence extended far b Application context: Furthermore, the Applicant argues that it is the RPD and not he who speculated in that regard when it found that the evidence was insufficient to conclude that it was “more probable than not that [Makhan Singh’s] influen Evidence spans paragraphs 23-25. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5144060` offsets `183-188`; context: He adds that the RPD’s decision on the issue of IFA is unreasonable for the following reasons.
- Evidence: `party_position` cue `submits` at chunk `5144060` offsets `19-26`; context: [23] The Applicant submits that the RPD erred in fact and in law in concluding that he could live safely in
New Delhi ,
Bangalore or
Calcutta
.
- Evidence: `issue` cue `issue` at chunk `5144061` offsets `25-30`; context: [24] With regards to the issue of the IFA, according to the Applicant, the RPD erred when it concluded that his fear was subjective and not objectively well-founded, as his personal circumstances combined with the prevalent country conditions all amounted to a real and objective well-founded fear of danger to his life if he were to return to
India
.
- Evidence: `party_position` cue `argues` at chunk `5144062` offsets `135-141`; context: [25] Contrary to the RPD’s finding pertaining to the Applicant’s knowledge of how far Makhan Singh’s influence extended, the Applicant argues that he did indeed testify and confirm that the man’s influence extended far beyond his own district of Patiala.
- Evidence: `evidence_fact` cue `found that` at chunk `5144062` offsets `539-549`; context: Furthermore, the Applicant argues that it is the RPD and not he who speculated in that regard when it found that the evidence was insufficient to conclude that it was “more probable than not that [Makhan Singh’s] influence extends into other states where the cities mentioned as possible refuges are located.
- Evidence: `reasoning_application` cue `conclude` at chunk `5144062` offsets `583-591`; context: Furthermore, the Applicant argues that it is the RPD and not he who speculated in that regard when it found that the evidence was insufficient to conclude that it was “more probable than not that [Makhan Singh’s] influence extends into other states where the cities mentioned as possible refuges are located.

#### 24322:1:subtheme:5 · paragraphs 26-27

- Raw key terms: `applicant, argues, evidence, face, india, makhan, police, singh`
- Display key terms: `argues, face, india, makhan, police, singh`
- Argument roles: `evidence_fact, issue, party_position`
- Explanation: Observed roles: evidence_fact, issue, party_position Display terms: argues, face, india, makhan, police, singh Position/evidence statements: The Applicant also submits that the RPD failed to take into consideration a number of factors in the Applicant’s evidence which served to support the conclusion that it is more probable than not that his life would be at | [27] The Applicant argues that his fear was well-founded and not speculative, in that the RPD should have considered the evidence relating to the fact that the police were used by Makhan Singh when they arrested his fath Evidence spans paragraphs 26-27. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5144063` offsets `474-481`; context: He argues that the RPD should have examined these elements when determining whether relocation was a viable option for the Applicant.
- Evidence: `party_position` cue `submits` at chunk `5144063` offsets `135-142`; context: The Applicant also submits that the RPD failed to take into consideration a number of factors in the Applicant’s evidence which served to support the conclusion that it is more probable than not that his life would be at risk in the cities mentioned as possible refuges by the RPD.
- Evidence: `evidence_fact` cue `evidence` at chunk `5144063` offsets `77-85`; context: [26] According to the Applicant, the RPD’s analysis on its assessment of the evidence was deficient and incomplete.
- Evidence: `party_position` cue `argues` at chunk `5144064` offsets `19-25`; context: [27] The Applicant argues that his fear was well-founded and not speculative, in that the RPD should have considered the evidence relating to the fact that the police were used by Makhan Singh when they arrested his father in 2005.
- Evidence: `evidence_fact` cue `evidence` at chunk `5144064` offsets `121-129`; context: [27] The Applicant argues that his fear was well-founded and not speculative, in that the RPD should have considered the evidence relating to the fact that the police were used by Makhan Singh when they arrested his father in 2005.

#### Section text

Singh v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2013-09-26
Neutral citation
2013 FC 988
File numbers
IMM-826-13
Decision Content
Date: 20130926
Docket: IMM-826-13
Citation: 2013 FC 988
Montréal
,
Quebec
, September 26, 2013
PRESENT: The Honourable Mr. Justice Simon Noël
BETWEEN:
BARINDER SINGH
Applicant
and
THE MINISTER OF CITIZENSHIP
AND IMMIGRATION
Respondent
REASONS FOR JUDGMENT AND JUDGMENT

[1] This is an application for judicial review under subsection 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [“IRPA”] of a decision of the Refugee Protection Division [“RPD”], dated December 21, 2012 that the Applicant was neither a “Convention refugee” within the meaning of section 96 of the IRPA nor a “person in need of protection” under subsection 97(1) of the IRPA.

[2] Counsel for the Applicant presented a motion to be removed as solicitor of record due to the facts that the Applicant is not reachable, that his phone has been cancelled and that it is known in the Punjabi community that he has left the country. This motion was presented the day on which the judicial review was to be heard. Having granted the motion, it was then suggested by counsel for the Respondent that I dismiss the judicial review. I suggested that it was in the interest of justice that I hear it in the absence of the Applicant since the Applicant is not reachable and that the submissions of his counsel are already part of the Applicant’s motion record and that the issue raised is limited to the internal flight alternative [“IFA”].
I. Facts

[3] The Applicant is a 22-year-old citizen of
India
. He claims to be a “Convention refugee” and a “person in need of protection” within the meaning of section 96 and subsection 97(1) of the IRPA. The RPD however analyzed the claim solely under subsection 97(1) of the IRPA.

[4] The Applicant came to
Canada when he was 17 years old, via
Italy
where he had become a permanent resident in 2008.

[5] The Applicant’s problems in
India began when his father leased his land to Mr. Makhan Singh before going to
Italy
. A few months later, however, Makhan Singh stopped paying rent. The Applicant’s father then proceeded to cancel the lease agreement and take back the land. Mr. Makhan Singh, who it is alleged is an influential person, was not happy with the situation. The Applicant’s mother heard that he planned to kidnap her son.

[6] On one occasion, on December 14, 2007, the Applicant was beaten up on his way home from school. The people who attacked him told him they did so because his father humiliated Makhan Singh by taking back the land. The sarpanch informed the police about the incident, but they did not take it seriously. A second visit to the police did not foster the matter any further.

[7] The Applicant’s father got the family members’ permanent resident visas and the family arrived in
Italy
on May 21, 2008. There, the Applicant encountered troubles with boys who were attending his school and he was even attacked by some of them on one occasion. The Applicant’s father decided to send his son, the Applicant, to
Canada
where his uncle was living for a while.

[8] When he wanted to return to
Italy
, the Applicant was told by his father that it was too risky. He consequently made a refugee application on July 20, 2009.

[9] Since arriving in
Canada
, the Applicant has learned from his father that Makhan Singh is vowing to get even with the family.
II. Decision under review

[10] The RPD was satisfied with the evidence submitted pertaining to the Applicant’s identity.

[11] The RPD determined that the Applicant is neither a Convention refugee nor a person in need of protection pursuant to section 96 and subsection 97(1) of the IRPA.

[12] The RPD noted that according to documentary evidence submitted regarding the requirements for residence in
Italy
, a permanent resident who is absent from the country for 12 months or more loses permanent resident status. This was the case of the Applicant.

[13] The RPD examined the Applicant’s exclusion status under Article 1E of Article 1 of the Convention Against Torture and Other Cruel, Inhuman or Degrading Treatment or Punishment, and concluded that he was not excluded given that he had come to Canada as a minor and that the decision was not his, but his father’s. The RPD went on to find that the loss of status was involuntary.

[14] Furthermore, the RPD noted that the claim was based on a personal vendetta of Makhan Singh against the Applicant and his family and, as such, the animosity between these people did not fall within any of the grounds listed in section 96 of the IRPA.

[15] According to the RPD, even though the Applicant claimed that Makhan Singh is influential with police and politicians and that he uses the police to exact revenge on people, there wasn’t enough evidence that the police were intending to make any false case against the Applicant for any reason that would engage one of the grounds within section 96 of the IRPA.

[16] Consequently, the RPD analyzed the claim solely under subsection 97(1) of the IRPA.

[17] The RPD noted that the determinative issue in the claim lay in the availability of an IFA and concluded to the existence of multiple IFAs, namely
New Delhi ,
Bangalore and
Calcutta
.

[18] The Applicant expressed fears on several counts with regards to the possibility of relocating to either one of these cities, but the RPD found the Applicant’s various fears to be subjective and not objectively well-founded. First, the Applicant had alleged that he would be afraid of the police if he had to move to
New Delhi or
Bangalore or
Calcutta
, claiming that he did not know how far Makhan Singh’s influence extends and that he was afraid that his goons could take him and bring him back to Makhan Singh. The RPD found that the basis of that fear was speculative and that there was insufficient evidence to conclude that it was more probable than not that Makhan Singh’s influence extends to other states mentioned as possible refuges.

[19] Second, the RPD considered another of the Applicant’s allegations according to which he was afraid that when the police of the aforementioned cities were to run a background verification on him, that they would have him brought back to Makhan Singh. Based on objective evidence, the RPD found that, while police inspections are made in various cities because of the obligation of landlords and employers to report newcomers, it was not more likely than not that the police would bring forward a false accusation in the Applicant’s case. Moreover, the RPD stated that the police presumably could have done that while the Applicant was still in
India
, but they did not, and therefore concluded that it was unlikely they would do so today.

[20] Also, the RPD concluded that it was not necessarily more likely that the Applicant would face a risk to his life or cruel and unusual punishment or torture, should he relocate to
New Delhi or
Bangalore or
Calcutta
.

[21] Ultimately, the RPD determined that it was reasonable for the Applicant to relocate, as he is a young adult of 22 years of age and, given that in the Applicant’s circumstances, there is no evidence of hardship in relocating that would give rise to a risk to life or safety, as required by the reasonableness test for an IFA.

[22] Finally, the RPD concluded that the Applicant had failed in his burden of establishing that it was more likely than not that he would face a risk to his life or cruel and usual punishment or torture in the event of him returning to
India
.
III. Applicant’s submissions

[23] The Applicant submits that the RPD erred in fact and in law in concluding that he could live safely in
New Delhi ,
Bangalore or
Calcutta
. He adds that the RPD’s decision on the issue of IFA is unreasonable for the following reasons.

[24] With regards to the issue of the IFA, according to the Applicant, the RPD erred when it concluded that his fear was subjective and not objectively well-founded, as his personal circumstances combined with the prevalent country conditions all amounted to a real and objective well-founded fear of danger to his life if he were to return to
India
.

[25] Contrary to the RPD’s finding pertaining to the Applicant’s knowledge of how far Makhan Singh’s influence extended, the Applicant argues that he did indeed testify and confirm that the man’s influence extended far beyond his own district of Patiala. The Applicant further submits that the RPD failed to take into consideration Makhan Singh’s influence outside of
Patiala
when assessing the possible IFAs available to the Applicant. Furthermore, the Applicant argues that it is the RPD and not he who speculated in that regard when it found that the evidence was insufficient to conclude that it was “more probable than not that [Makhan Singh’s] influence extends into other states where the cities mentioned as possible refuges are located.”

[26] According to the Applicant, the RPD’s analysis on its assessment of the evidence was deficient and incomplete. The Applicant also submits that the RPD failed to take into consideration a number of factors in the Applicant’s evidence which served to support the conclusion that it is more probable than not that his life would be at risk in the cities mentioned as possible refuges by the RPD. He argues that the RPD should have examined these elements when determining whether relocation was a viable option for the Applicant. Amongst others, the numerous factors adduced relate to Makhan Singh’s conduct and his interest in the whereabouts of the Applicant. The mentioned factors also speak of the dangers which the Applicant would face in India and to the problem of police corruption in the country whereby police frequently arrest and detain people at the behest of powerful local figures and that manifestations of corrupt behaviour are rarely prosecuted.

[27] The Applicant argues that his fear was well-founded and not speculative, in that the RPD should have considered the evidence relating to the fact that the police were used by Makhan Singh when they arrested his father in 2005. He adds that the mere fact that the police could have laid false accusations against the Applicant while he was still in
India
did not mean that the Applicant faces no harm today. He maintains that were he to return to
India
today he would still face danger as the “opportunity and motive” exist.

## 24322:2 · paragraphs 28-34

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `2eeba648a13fc153f4f37931869796392ebab88ccae129f5b1db04a82ab274df`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 24322:2:subtheme:1 · paragraphs 28-31

- Raw key terms: `applicant, respondent, according, argues, community, evidence, failed, india`
- Display key terms: `according, argues, community, failed, india`
- Argument roles: `evidence_fact, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, party_position, reasoning_application Display terms: according, argues, community, failed, india Position/evidence statements: [29] The Applicant also argues that being only 22 years of age and having left India as a minor it would be unreasonable to expect him to move to a large urban area away from his protective community, thereby making the  | [30] The Respondent submits that the RPD’s decision to reject the Applicant’s claim was reasonable. Application context: He also claims that there is no evidence to conclude on a balance of probabilities that Makhan Singh’s influence extends to other states in India than his own or that the police would act at the behest of Makhan Singh to Evidence spans paragraphs 28-31. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `evidence` at chunk `5144065` offsets `236-244`; context: [28] According to the Applicant, the RPD also failed to consider various elements of the cultural context of the Applicant, including the limited education of the Applicant, the fact that his education has been interrupted, the lack of evidence before the RPD pertaining to the Applicant’s proficiency in Hindi, the fact that the Applicant has no ties with the cities mentioned as refuges and the fact that since he lived in a small farming village the Applicant was part of a closely knit and protective community.
- Evidence: `party_position` cue `argues` at chunk `5144066` offsets `24-30`; context: [29] The Applicant also argues that being only 22 years of age and having left
India
as a minor it would be unreasonable to expect him to move to a large urban area away from his protective community, thereby making the second prong of the IFA test unreasonable.
- Evidence: `party_position` cue `submits` at chunk `5144067` offsets `20-27`; context: [30] The Respondent submits that the RPD’s decision to reject the Applicant’s claim was reasonable.
- Evidence: `party_position` cue `argues` at chunk `5144068` offsets `66-72`; context: [31] In this regard, relying on the RPD’s reasons, the Respondent argues that it is highly unlikely, and speculative that Makhan Singh could or would pursue the Applicant in either of the proposed IFAs.
- Evidence: `evidence_fact` cue `evidence` at chunk `5144068` offsets `299-307`; context: He also claims that there is no evidence to conclude on a balance of probabilities that Makhan Singh’s influence extends to other states in India than his own or that the police would act at the behest of Makhan Singh to locate the Applicant and bring him to Makhan Singh, and that there is no evidence of hardship in relocating the Applicant that would give rise to a risk to his life or safety.
- Evidence: `reasoning_application` cue `conclude` at chunk `5144068` offsets `311-319`; context: He also claims that there is no evidence to conclude on a balance of probabilities that Makhan Singh’s influence extends to other states in India than his own or that the police would act at the behest of Makhan Singh to locate the Applicant and bring him to Makhan Singh, and that there is no evidence of hardship in relocating the Applicant that would give rise to a risk to his life or safety.

#### 24322:2:subtheme:2 · paragraphs 32-34

- Raw key terms: `applicant, relocate, respondent, according, adds, argues, bangalore, bore`
- Display key terms: `relocate, according, adds, argues, bangalore, bore`
- Argument roles: `governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: governing_rule, issue, party_position, reasoning_application Display terms: relocate, according, adds, argues, bangalore, bore Position/evidence statements: [32] The Respondent argues that jurisprudence sets out a two-pronged test to determine whether an IFA exists or not. Rule/authority context: [32] The Respondent argues that jurisprudence sets out a two-pronged test to determine whether an IFA exists or not. Application context: According to the Respondent, the Applicant’s situation is consistent with such jurisprudence and therefore meets the two-pronged test. Evidence spans paragraphs 32-34. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5144069` offsets `87-94`; context: [32] The Respondent argues that jurisprudence sets out a two-pronged test to determine whether an IFA exists or not.
- Evidence: `party_position` cue `argues` at chunk `5144069` offsets `20-26`; context: [32] The Respondent argues that jurisprudence sets out a two-pronged test to determine whether an IFA exists or not.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `5144069` offsets `32-45`; context: [32] The Respondent argues that jurisprudence sets out a two-pronged test to determine whether an IFA exists or not.
- Evidence: `reasoning_application` cue `therefore` at chunk `5144069` offsets `214-223`; context: According to the Respondent, the Applicant’s situation is consistent with such jurisprudence and therefore meets the two-pronged test.

#### Section text

[28] According to the Applicant, the RPD also failed to consider various elements of the cultural context of the Applicant, including the limited education of the Applicant, the fact that his education has been interrupted, the lack of evidence before the RPD pertaining to the Applicant’s proficiency in Hindi, the fact that the Applicant has no ties with the cities mentioned as refuges and the fact that since he lived in a small farming village the Applicant was part of a closely knit and protective community.

[29] The Applicant also argues that being only 22 years of age and having left
India
as a minor it would be unreasonable to expect him to move to a large urban area away from his protective community, thereby making the second prong of the IFA test unreasonable. He finishes by stating that, having lost his permanent resident status in
Italy
, he faced a future of poverty with no hope.
IV. Respondent’s submissions

[30] The Respondent submits that the RPD’s decision to reject the Applicant’s claim was reasonable. According to the Respondent, the Applicant clearly failed to establish that it is more likely than not that he would face a risk to his life or cruel and unusual punishment or torture should he relocate in
New Delhi ,
Bangalore or
Calcutta
.

[31] In this regard, relying on the RPD’s reasons, the Respondent argues that it is highly unlikely, and speculative that Makhan Singh could or would pursue the Applicant in either of the proposed IFAs. The Respondent claims that the Applicant’s fear is speculative. He also claims that there is no evidence to conclude on a balance of probabilities that Makhan Singh’s influence extends to other states in India than his own or that the police would act at the behest of Makhan Singh to locate the Applicant and bring him to Makhan Singh, and that there is no evidence of hardship in relocating the Applicant that would give rise to a risk to his life or safety.

[32] The Respondent argues that jurisprudence sets out a two-pronged test to determine whether an IFA exists or not. According to the Respondent, the Applicant’s situation is consistent with such jurisprudence and therefore meets the two-pronged test. With regards to the foregoing, following the test, the Applicant bore the onus of establishing that an IFA did not in fact exist and that it was objectively unreasonable or unduly harsh for him to relocate to the IFA in question. The “objectively unreasonable” standard is subject to a very high threshold which was not satisfied by the Applicant. The Respondent adds that this standard is to be evaluated in a flexible manner with regard to the relevant country conditions and the Applicant’s personal circumstances, and that the difficulties inherent to being displaced are not considered to be unreasonable.

[33] The Applicant did not establish the serious possibility of a risk to his life or that he would suffer cruel or unusual punishment should he relocate to one of the proposed refuges.

[34] The Respondent is of the view that the RPD’s finding that the Applicant can relocate to an IFA in
New Delhi ,
Bangalore or
Calcutta
is reasonable.


## 24322:3 · paragraphs 35-36

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `c9d4c6c6646bdcaf873ae62df4fd73d5bb830ff32dea86ea3d821d07e9fd9148`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 24322:3:subtheme:1 · paragraphs 35-36

- Raw key terms: `issue, applicant, available, bangalore, calcutta, concluding, delhi, erred`
- Display key terms: `available, bangalore, calcutta, concluding, delhi, erred`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: available, bangalore, calcutta, concluding, delhi, erred Evidence spans paragraphs 35-36. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5144072` offsets `35-40`; context: [35] The present matter raises the issue of whether the RPD erred in concluding that an IFA was available to the Applicant in
New Delhi ,
Bangalore or
Calcutta
.

#### Section text

V. Issue

[35] The present matter raises the issue of whether the RPD erred in concluding that an IFA was available to the Applicant in
New Delhi ,
Bangalore or
Calcutta
.


## 24322:4 · paragraphs 37-38

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `e1854efcccfa2e056e832e468e506b12f88006e3ceca02707aac4b9fc2315a2f`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 24322:4:subtheme:1 · paragraphs 37-38

- Raw key terms: `standard, brunswick, determination, dunsmuir, para, reasonableness, review, reviewed`
- Display key terms: `standard, brunswick, determination, dunsmuir, para, reasonableness, review, reviewed`
- Argument roles: `governing_rule`
- Explanation: Observed roles: governing_rule Display terms: standard, brunswick, determination, dunsmuir, para, reasonableness, review, reviewed Rule/authority context: [36] The RPD’s IFA determination is to be reviewed under the standard of reasonableness (Dunsmuir v New Brunswick , 2008 SCC 9 at para 53, [2008] 1 SCR 190). Evidence spans paragraphs 37-38. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `under` at chunk `5144073` offsets `51-56`; context: [36] The RPD’s IFA determination is to be reviewed under the standard of reasonableness (Dunsmuir v
New Brunswick
, 2008 SCC 9 at para 53, [2008] 1 SCR 190).

#### Section text

VI. Standard of review

[36] The RPD’s IFA determination is to be reviewed under the standard of reasonableness (Dunsmuir v
New Brunswick
, 2008 SCC 9 at para 53, [2008] 1 SCR 190).


## 24322:5 · paragraphs 39-40

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `3c9ef8fd4927e642d8f4f47f0b44e6e7d1984eff899aa70e2193fc987592a972`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 24322:5:subtheme:1 · paragraphs 39-40

- Raw key terms: `acws, analysis, appeal, applicant, balance, canada, circumstances, conditions`
- Display key terms: `acws, analysis, balance, circumstances, conditions`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: acws, analysis, balance, circumstances, conditions Evidence spans paragraphs 39-40. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5144074` offsets `106-113`; context: [37] The Federal Court of Appeal established a two-pronged test which the courts must follow to determine whether an IFA exists or not.

#### Section text

VII. Analysis

[37] The Federal Court of Appeal established a two-pronged test which the courts must follow to determine whether an IFA exists or not. First, the RPD must be satisfied, on a balance of probabilities, that there is no serious possibility of the Applicant being persecuted in the part of the country to which it finds an IFA exists, and second, conditions in that part of the country must be such that it would not be unreasonable, in all the circumstances, for the Applicant to seek refuge there (see Rasaratnam v Canada (Minister of Employment and Immigration) (1991), 140 NR 138, 31 ACWS (3d) 139 (FCA); Thirunavukkarasu v Canada (Minister of Employment and Immigration) (1993), 22 Imm LR (2d) 241, 109 DLR (4th) 682 (FCA)).

## 24322:6 · paragraphs 41-46

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `7caa357d90e6724258d12c2cc1ff7ad8f2aff08d086e6612ad2c01cacb2afabb`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 24322:6:subtheme:1 · paragraphs 41-43

- Raw key terms: `applicant, evidence, life, canada, circumstances, conditions, country, failed`
- Display key terms: `life, circumstances, conditions, country, failed`
- Argument roles: `counterargument_limitation, evidence_fact, party_position`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, party_position Display terms: life, circumstances, conditions, country, failed Position/evidence statements: To the contrary, the Applicant argued that his fear was well-founded, given his personal circumstances and the prevalent country conditions he would face in India . Evidence spans paragraphs 41-43. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `party_position` cue `argued` at chunk `5144075` offsets `358-364`; context: To the contrary, the Applicant argued that his fear was well-founded, given his personal circumstances and the prevalent country conditions he would face in
India
.
- Evidence: `evidence_fact` cue `found that` at chunk `5144075` offsets `46-56`; context: [38] With regards to the first prong, the RPD found that the Applicant’s fear is subjective and not objectively well-founded and concluded that it was not more likely than not that the Applicant would face a risk to his life or cruel and unusual punishment or torture should he relocate to
New Delhi or
Bangalore or
Calcutta
.
- Evidence: `counterargument_limitation` cue `However` at chunk `5144075` offsets `584-591`; context: However, there is a presumption that, although they were not directly referred to by the RPD, they were nonetheless given due consideration (see Florea v
Canada
(Minister of Employment and Immigration), [1993] FCJ 598 (FCA)).
- Evidence: `evidence_fact` cue `found that` at chunk `5144076` offsets `46-56`; context: [39] As for the second prong of test, the RPD found that it would be reasonable for the Applicant to relocate, as there was no evidence of hardship in his particular circumstances that would give rise to a risk to life or safety.
- Evidence: `evidence_fact` cue `evidence` at chunk `5144077` offsets `526-534`; context: Furthermore, the Applicant was required to produce actual and concrete evidence of such conditions (Ranganathan v
Canada
(Minister of Citizenship and Immigration) (2000), 11 Imm LR (3d) 142 at para 15, 266 NR 380 (FCA)).

#### 24322:6:subtheme:2 · paragraphs 44-45

- Raw key terms: `applicant, court, acceptable, alternatives, answering, based, brunswick, canada`
- Display key terms: `acceptable, alternatives, answering, based, brunswick`
- Argument roles: `evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, reasoning_application Display terms: acceptable, alternatives, answering, based, brunswick Application context: [42] The Applicant therefore failed to satisfy this Court that the internal flight alternatives are unreasonable and that the RPD committed an error warranting this Court's intervention. Evidence spans paragraphs 44-45. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5144078` offsets `9-14`; context: [41] The issue comes down to answering the following question, as previously formulated by this Court: Is it objectively reasonable to expect the Applicant to move to a different part of the country?
- Evidence: `evidence_fact` cue `evidence` at chunk `5144078` offsets `319-327`; context: (Krasniqi v
Canada
(Minister of Citizenship and Immigration), 2010 FC 350, at para 44, [2010] FCJ No 410) Based on the evidence with which it had been presented, the RPD found that such was not the case for the Applicant, and this “decision falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and the law" (see Dunsmuir v New Brunswick, 2008 SCC 9, [2008] 1 SCR 190 at para 47) despite the Applicant’s submissions.
- Evidence: `reasoning_application` cue `therefore` at chunk `5144079` offsets `19-28`; context: [42] The Applicant therefore failed to satisfy this Court that the internal flight alternatives are unreasonable and that the RPD committed an error warranting this Court's intervention.

#### 24322:6:subtheme:3 · paragraphs 46-46

- Raw key terms: `assessment, call, case, certified, facts, general, importance, issue`
- Display key terms: `assessment, call, case, certified, facts, importance`
- Argument roles: `issue, reasoning_application`
- Explanation: Observed roles: issue, reasoning_application Display terms: assessment, call, case, certified, facts, importance Application context: Therefore, no question will be certified. Evidence spans paragraphs 46-46. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5144080` offsets `13-18`; context: [43] The IFA issue does not raise any matter of general importance that could call for a certified question.
- Evidence: `reasoning_application` cue `Therefore` at chunk `5144080` offsets `189-198`; context: Therefore, no question will be certified.

#### Section text

[38] With regards to the first prong, the RPD found that the Applicant’s fear is subjective and not objectively well-founded and concluded that it was not more likely than not that the Applicant would face a risk to his life or cruel and unusual punishment or torture should he relocate to
New Delhi or
Bangalore or
Calcutta
. To the contrary, the Applicant argued that his fear was well-founded, given his personal circumstances and the prevalent country conditions he would face in
India
. He adds that the RPD failed to consider numerous factors found in the Applicant’s evidence. However, there is a presumption that, although they were not directly referred to by the RPD, they were nonetheless given due consideration (see Florea v
Canada
(Minister of Employment and Immigration), [1993] FCJ 598 (FCA)).

[39] As for the second prong of test, the RPD found that it would be reasonable for the Applicant to relocate, as there was no evidence of hardship in his particular circumstances that would give rise to a risk to life or safety. The Applicant failed to present evidence of undue hardship which could render the second prong of the IFA test unreasonable.

[40] As submitted by the Respondent, the Applicant bore the onus of establishing that it is objectively unreasonable to expect him to seek safety in a different part of the country before seeking a haven in
Canada
or elsewhere. Also, the threshold for the “objectively unreasonable” standard is very high and requires, at a minimum, the proof of adverse conditions which would jeopardize the life and safety of the Applicant in relocating to a safe area. Furthermore, the Applicant was required to produce actual and concrete evidence of such conditions (Ranganathan v
Canada
(Minister of Citizenship and Immigration) (2000), 11 Imm LR (3d) 142 at para 15, 266 NR 380 (FCA)).

[41] The issue comes down to answering the following question, as previously formulated by this Court: Is it objectively reasonable to expect the Applicant to move to a different part of the country? (Krasniqi v
Canada
(Minister of Citizenship and Immigration), 2010 FC 350, at para 44, [2010] FCJ No 410) Based on the evidence with which it had been presented, the RPD found that such was not the case for the Applicant, and this “decision falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and the law" (see Dunsmuir v New Brunswick, 2008 SCC 9, [2008] 1 SCR 190 at para 47) despite the Applicant’s submissions.

[42] The Applicant therefore failed to satisfy this Court that the internal flight alternatives are unreasonable and that the RPD committed an error warranting this Court's intervention.

[43] The IFA issue does not raise any matter of general importance that could call for a certified question. It is a case that raises only an assessment of the facts in relation to an IFA. Therefore, no question will be certified.


## 24322:7 · paragraphs 47-48

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `aa030d610e71bac487e8a864506ca1d624d80fcb5f842bb3e7d93bba6a321d19`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 24322:7:subtheme:1 · paragraphs 47-48

- Raw key terms: `application, barinder, cause, certified, citizenship, court, date, denied`
- Display key terms: `barinder, certified, date, denied`
- Argument roles: `disposition, issue`
- Explanation: Observed roles: disposition, issue Display terms: barinder, certified, date, denied Operative outcome context: JUDGMENT THIS COURT’S JUDGMENT is that this application for judicial review is denied. Evidence spans paragraphs 47-48. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5144080` offsets `321-329`; context: No question is certified.
- Evidence: `disposition` cue `denied` at chunk `5144080` offsets `310-316`; context: JUDGMENT
THIS COURT’S JUDGMENT is that this application for judicial review is denied.

#### Section text

JUDGMENT
THIS COURT’S JUDGMENT is that this application for judicial review is denied. No question is certified.
“Simon Noël”
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET: IMM-826-13
STYLE OF CAUSE: BARINDER SINGH v THE MINISTER OF
CITIZENSHIP AND IMMIGRATION
PLACE OF HEARING: Montréal, Québec
DATE OF HEARING: September 25, 2013
REASONS FOR 

## 24322:8 · paragraphs 49-49

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `eb131b916a22b0cc9138eb715669251894df81bcc63d11ca28b160d94a5b2a7f`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 24322:8:subtheme:1 · paragraphs 49-49

- Raw key terms: `appearances, attorney, canada, dated, deputy, general, janura, judgment`
- Display key terms: `dated, deputy, janura`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: dated, deputy, janura No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 49-49. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT
AND JUDGMENT: NOËL J.
DATED: September 26, 2013
APPEARANCES:
Pavol Janura
FOR THE RESPONDENT
SOLICITORS OF RECORD:
William F. Pentney
Deputy Attorney General of
Canada
Montréal
,
QC
FOR THE RESPONDENT
