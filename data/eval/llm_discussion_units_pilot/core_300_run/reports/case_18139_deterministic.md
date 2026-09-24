# Discussion Units: case 18139

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **59**
- Continuity pairs: **58**
- Discussion Units: **3**
- Paragraph source hashes: **59**
- Sub-themes: **15**

## 18139:1 · paragraphs 0-4

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `492db484cc74a35b3374647e1b24839383d6693a85090b24a21d8d8bc8febd12`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 18139:1:subtheme:1 · paragraphs 0-1

- Raw key terms: `applicant, court, decision, federal, immigration, amended, application, august`
- Display key terms: `federal, amended, august`
- Argument roles: `evidence_fact, governing_rule`
- Explanation: Observed roles: evidence_fact, governing_rule Display terms: federal, amended, august Rule/authority context: [1] This is an application under section 18. Evidence spans paragraphs 0-1. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `determined that` at chunk `4859242` offsets `287-302`; context: F-7 as amended, for judicial review of a decision made by the Convention Refugee Determination Division of the Immigration and Refugee Board (the tribunal) dated August 11, 1999, wherein the tribunal determined that the applicant was not a Convention refugee.
- Evidence: `governing_rule` cue `under` at chunk `4859242` offsets `27-32`; context: [1] This is an application under section 18.

#### 18139:1:subtheme:2 · paragraphs 2-3

- Raw key terms: `appearance, applicant's, because, bulgaria, bulgarian, concluded, ethnicity, held`
- Display key terms: `appearance, applicant's, because, bulgaria, bulgarian, concluded, ethnicity`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, issue, reasoning_application Display terms: appearance, applicant's, because, bulgaria, bulgarian, concluded, ethnicity Application context: However, from the moment they moved in, they faced resentment and hostility from their neighbours because of their Roma ethnicity. | The tribunal also determined that the applicant was not reliable nor trustworthy, and held that he left Bulgaria for economic reasons, and not because of a fear of persecution. Operative outcome context: He was denied access to his mother as she was dying. Evidence spans paragraphs 2-3. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4859243` offsets `3696-3703`; context: The prosecutor visited him to inquire whether he had "changed his mind.
- Evidence: `reasoning_application` cue `because` at chunk `4859243` offsets `1477-1484`; context: However, from the moment they moved in, they faced resentment and hostility from their neighbours because of their Roma ethnicity.
- Evidence: `counterargument_limitation` cue `However` at chunk `4859243` offsets `1379-1386`; context: However, from the moment they moved in, they faced resentment and hostility from their neighbours because of their Roma ethnicity.
- Evidence: `disposition` cue `denied` at chunk `4859243` offsets `2096-2102`; context: He was denied access to his mother as she was dying.
- Evidence: `issue` cue `Issues` at chunk `4859244` offsets `462-468`; context: Issues
a.
- Evidence: `evidence_fact` cue `determined that` at chunk `4859244` offsets `300-315`; context: The tribunal also determined that the applicant was not reliable nor trustworthy, and held that he left Bulgaria for economic reasons, and not because of a fear of persecution.
- Evidence: `reasoning_application` cue `because` at chunk `4859244` offsets `425-432`; context: The tribunal also determined that the applicant was not reliable nor trustworthy, and held that he left Bulgaria for economic reasons, and not because of a fear of persecution.

#### 18139:1:subtheme:3 · paragraphs 4-4

- Raw key terms: `adding, although, analysis, analyzed, applicant, applicant's, approach, claim`
- Display key terms: `adding, although, analysis, analyzed, applicant's, approach`
- Argument roles: `counterargument_limitation, issue, party_position`
- Explanation: Observed roles: counterargument_limitation, issue, party_position Display terms: adding, although, analysis, analyzed, applicant's, approach Position/evidence statements: [4] The tribunal determined at page 5 of the decision that the applicant's ethnicity, his credibility, and his failure to claim elsewhere were the pertinent issues in this claim. Evidence spans paragraphs 4-4. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4859245` offsets `157-163`; context: [4] The tribunal determined at page 5 of the decision that the applicant's ethnicity, his credibility, and his failure to claim elsewhere were the pertinent issues in this claim.
- Evidence: `party_position` cue `claim` at chunk `4859245` offsets `122-127`; context: [4] The tribunal determined at page 5 of the decision that the applicant's ethnicity, his credibility, and his failure to claim elsewhere were the pertinent issues in this claim.
- Evidence: `counterargument_limitation` cue `Although` at chunk `4859245` offsets `179-187`; context: Although the tribunal analyzed each issue separately, its conclusion that the applicant was not credible permeated the entire analysis.

#### Section text

Valtchev v. Canada (Minister of Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2001-07-06
Neutral citation
2001 FCT 776
File numbers
IMM-4497-99
Notes
Digest
Decision Content
Date: 20010706
Docket: IMM-4497-99
Neutral Citation: 2001 FCT 776
BETWEEN:
ROUSKO VALTCHEV,
Applicant,
- and -
THE MINISTER OF CITIZENSHIP AND IMMIGRATION,
Respondent.
REASONS FOR ORDER and ORDER
Muldoon, J .
1. Introduction

[1] This is an application under section 18.1 of the Federal Court Act, R.S.C. 1985, c.F-7 as amended, for judicial review of a decision made by the Convention Refugee Determination Division of the Immigration and Refugee Board (the tribunal) dated August 11, 1999, wherein the tribunal determined that the applicant was not a Convention refugee.
2. Statement of Facts

[2] The tribunal summarized the applicant's claim for Convention refugee status starting at page 1 of the decision:
BACKGROUND
The claimant is a 51 year-old married male and a citizen of Bulgaria. His wife, a son, and a daughter, continue to reside in Bulgaria.
...
SUMMARY OF THE CLAIMANT'S ALLEGATIONS
The claimant was born in Haskovo, Bulgaria, in 1948. He attended school for 11 years and trained to work as a machinist.
The claimant alleges he is of gypsy (Roma) ethnicity. While he was growing up, he experienced continuing discrimination and harassment by reason of his Roma origins. During his compulsory military service over the years 1967 to 1969, he alleged that all the dirty and difficult jobs were given to him and not to ethnic Bulgarians. The same problems confronted him in the area of employment where he felt that difficult, dirty, short-duration jobs were given to him and to other Romas in contrast to what was available for ethnic Bulgarians. For 20 years the claimant worked in construction and as a cleaner, experiencing constant layoffs and job relocations.
In the winter of 1989, he and his family were evicted from their housing in Sofia and literally turned out into the street. They spent the next several years living in a wooden shack and not until March 1993 was the family able to secure reasonable accommodation in a proper apartment building. However, from the moment they moved in, they faced resentment and hostility from their neighbours because of their Roma ethnicity. Less than a year after occupying their new apartment, they found themselves served with an eviction notice. The claimant and his family decided to resist the order. Neighbours set woodwork in the building on fire and accused the claimant's family (in particular, the claimant's mother) of responsibility. Then his mother was reported to the authorities as senile and forcibly removed to a mental hospital where she was poorly treated and became ill. The claimant wrote to health authorities protesting his mother's situation and in consequence, the police began persecuting him. He was denied access to his mother as she was dying. The claimant wrote a complaint to the Minister of Health. After that action, police came to the claimant's home, searched it and arrested him. He was kept in police custody for two nights. beaten, and made to tear up his complaint before he was released.
The claimant turned to a Roma political party for assistance but he found the party powerless to assist him. In the winter of 1994/95 the claimant hid out in the village of Turnovo while he was working in the same area. However, the police discovered his whereabouts and, while he was at work on a building site, seized him and forced him into a car destined for Sofia. En route, his abductors struck him repeatedly, saying they would "knock some reason into his head." On arrival in Sofia, he was taken before a prosecutor who asked him to sign a statement saying that he was voluntarily relinquishing his apartment. He was told that if he cooperated, another apartment would be found for him and his family. But if he resisted, he and his family would be forcibly evicted. The claimant said he would not sign the statement before having a chance to discuss the matter with his family. At this, the prosecutor became infuriated and started to strike the claimant. Then he took out an arrest warrant and served it on the claimant. The claimant was taken to the cell where he was told to "think things over." During the night, he was taken to another cell occupied by three other men. In the morning the three men were released but the claimant was kept inside. The prosecutor visited him to inquire whether he had "changed his mind." The prosecutor made numerous threats against the claimant and released the claimant after making him sign a blank summons mandating a court appearance in June or July 1995.
As the claimant was leaving the building where he had been held, 4 men jumped him and forced him into car. The claimant was driven to a site outside Sofia. He recognized three of the men as his former cellmates. They had in their possession the declaration, which the claimant had been earlier told to sign by the prosecutor. The claimant was held for three days and three nights, beaten and threatened. On the third night he managed to bribe the fourth man (then the sole guard) and escape.
The claimant immediately telephoned his wife who informed him that his construction work brigade was soon leaving for an assignment in Russia, in the city of Samara. The claimant arranged to go there as well, and on August 12, 1995, he traveled to Samara. However, police learned where he was and had his company return him to Bulgaria. Once back in Sofia, the police renewed their efforts to force the claimant and his family to vacate their apartment. To achieve this, the claimant was continually made to attend at the police station and other family members were subjected to constant harassment.
Just before Easter, in April 1996, police raided the claimant's apartment when he was temporarily absent. They searched everywhere, leaving his family in a state of shock. They then produced a "protocol" for the search and compelled claimant's wife to sign it. They also advised the claimant's wife that if she wished to continue living, she would be well advised to leave the claimant.
Shortly after this episode, the claimant was arrested again and taken to the police station where he was told to sign a statement voluntarily giving up his apartment. He refused to comply. He was again sent to a cell where he was held overnight. The following day, renewed efforts were made to have him sign a statement but he refused to do so. He was finally released after a summons was issued for him and his family.
The claimant sought the assistance of a lawyer but initially could find no one who would take on his case because he was a gypsy. He also turned for assistance to a Roma Parliamentary Representative named Manush Romanov. After discussing his problems in detail with Mr. Romanov, the claimant concluded that while Mr. Romanov might be able to assist him in securing another apartment, he was impotent to redress the wrongs the claimant had already suffered and he could not resolve the claimant's larger fears and insecurities.
The claimant decided that he had to leave the country to safeguard his safety and security. He intended to go to Canada to seek asylum but there was no resident Canadian Embassy in Sofia and he felt it would be difficult to obtain a Canadian visa. He decided to go to the USA and he received an American visa in Sofia on August 7, 1996.
The claimant entered the USA and traveled to Las Vegas where he lived and worked until December 1996. He did not apply for asylum in the USA but instead, traveled north, with several other Bulgarian nationals, arriving at Douglas, B.C., and entering Canada on December 6, 1996. He claimed refugee status on arrival.

[3] The tribunal concluded that the applicant was unlikely to be Roma. Alternatively, the tribunal held that if he was Roma, his personal attributes, including his appearance and his assimilation into the Bulgarian population, reduced his risk of persecution to a mere possibility. The tribunal also determined that the applicant was not reliable nor trustworthy, and held that he left Bulgaria for economic reasons, and not because of a fear of persecution.
3. Issues
a. Did the tribunal err in assessing the applicant's credibility;
b. Did the tribunal err in assessing the applicant's ethnicity;
c. Did the tribunal err in assessing the applicant's delay in claiming refugee status; and
d. Did the tribunal demonstrate a reasonable apprehension of bias towards the applicant.
4. Credibility

[4] The tribunal determined at page 5 of the decision that the applicant's ethnicity, his credibility, and his failure to claim elsewhere were the pertinent issues in this claim. Although the tribunal analyzed each issue separately, its conclusion that the applicant was not credible permeated the entire analysis. For example, when discussing the applicant's ethnicity, the tribunal stated at page 6 that it "finds the history of persecution provided by the claimant not to be credible and thus it is difficult to approach his claimed ethnicity without substantial skepticism." When discussing the applicant's failure to claim for Convention refugee status in the United States, the tribunal stated at page 15 that "the panel finds the claimant's explanation for his sojourn in United States not credible", adding at page 16 that "when his delay in claiming is coupled to the other elements in his story that are also strongly wanting in credibility, a picture emerges of an opportunistic and untrustworthy witness."

## 18139:2 · paragraphs 5-18

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `6cd47e381da23b500063447b2ced11da0e8ada9c58b22739fca0272c5ab8fc7e`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 18139:2:subtheme:1 · paragraphs 5-14

- Raw key terms: `evidence, findings, refugee, applicant, based, decision, events, implausible`
- Display key terms: `findings, refugee, based, events, implausible`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, reasoning_application Display terms: findings, refugee, based, events, implausible Rule/authority context: Nevertheless, the Board is under a very clear duty to justify its credibility findings with specific and clear reference to the evidence. Application context: But the tribunal does not apply the Maldonado principle to this applicant, and repeatedly disregards his testimony, holding that much of it appears to it to be implausible. | A tribunal must be careful when rendering a decision based on a lack of plausibility because refugee claimants come from diverse cultures, and actions which appear implausible when judged from Canadian standards might be Operative outcome context: Justice Cullen quashed a decision of the tribunal after concluding that it erred because its plausibility findings were made without referring to the documentary evidence, and because they were made based on Canadian par Evidence spans paragraphs 5-14. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `counterargument_limitation` cue `However` at chunk `4859246` offsets `192-199`; context: However, the Court has a duty to interfere when findings of credibility are patently unreasonable, or when they are made based on erroneous findings of fact made in a perverse or capricious manner without regard for the material before it.
- Evidence: `evidence_fact` cue `testimony` at chunk `4859247` offsets `389-398`; context: But the tribunal does not apply the Maldonado principle to this applicant, and repeatedly disregards his testimony, holding that much of it appears to it to be implausible.
- Evidence: `reasoning_application` cue `apply` at chunk `4859247` offsets `310-315`; context: But the tribunal does not apply the Maldonado principle to this applicant, and repeatedly disregards his testimony, holding that much of it appears to it to be implausible.
- Evidence: `evidence_fact` cue `evidence` at chunk `4859248` offsets `365-373`; context: , if the facts as presented are outside the realm of what could reasonably be expected, or where the documentary evidence demonstrates that the events could not have happened in the manner asserted by the claimant.
- Evidence: `reasoning_application` cue `because` at chunk `4859248` offsets `552-559`; context: A tribunal must be careful when rendering a decision based on a lack of plausibility because refugee claimants come from diverse cultures, and actions which appear implausible when judged from Canadian standards might be plausible when considered from within the claimant's milieu.
- Evidence: `counterargument_limitation` cue `However` at chunk `4859248` offsets `171-178`; context: However, plausibility findings should be made only in the clearest of cases, i.
- Evidence: `evidence_fact` cue `evidence` at chunk `4859250` offsets `136-144`; context: Nevertheless, the Board is under a very clear duty to justify its credibility findings with specific and clear reference to the evidence.
- Evidence: `governing_rule` cue `under` at chunk `4859250` offsets `35-40`; context: Nevertheless, the Board is under a very clear duty to justify its credibility findings with specific and clear reference to the evidence.
- Evidence: `counterargument_limitation` cue `Nevertheless` at chunk `4859250` offsets `8-20`; context: Nevertheless, the Board is under a very clear duty to justify its credibility findings with specific and clear reference to the evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `4859251` offsets `721-729`; context: The Board will therefore err when it fails to refer to relevant evidence which could potentially refute their conclusions of implausibility.
- Evidence: `reasoning_application` cue `therefore` at chunk `4859251` offsets `526-535`; context: The appropriateness of a particular finding can therefore only be assessed if the Board's decision clearly identifies all of the facts which form the basis for their conclusions.
- Evidence: `counterargument_limitation` cue `fails` at chunk `4859251` offsets `694-699`; context: The Board will therefore err when it fails to refer to relevant evidence which could potentially refute their conclusions of implausibility.
- Evidence: `evidence_fact` cue `evidence` at chunk `4859252` offsets `226-234`; context: Justice Cullen quashed a decision of the tribunal after concluding that it erred because its plausibility findings were made without referring to the documentary evidence, and because they were made based on Canadian paradigms:
- Evidence: `reasoning_application` cue `because` at chunk `4859252` offsets `145-152`; context: Justice Cullen quashed a decision of the tribunal after concluding that it erred because its plausibility findings were made without referring to the documentary evidence, and because they were made based on Canadian paradigms:
- Evidence: `disposition` cue `quashed` at chunk `4859252` offsets `79-86`; context: Justice Cullen quashed a decision of the tribunal after concluding that it erred because its plausibility findings were made without referring to the documentary evidence, and because they were made based on Canadian paradigms:
- Evidence: `evidence_fact` cue `evidence` at chunk `4859253` offsets `131-139`; context: However, in making a finding of what was plausible or implausible the Refugee Division made no reference to the documentary evidence filed in support of the applicant, namely the Amnesty International reports.
- Evidence: `reasoning_application` cue `Therefore` at chunk `4859253` offsets `411-420`; context: Therefore, in my view, the failure to comment on the evidence filed, either in a negative or positive manner, seriously weakened the Refugee Division's decision and conclusions.
- Evidence: `counterargument_limitation` cue `However` at chunk `4859253` offsets `7-14`; context: However, in making a finding of what was plausible or implausible the Refugee Division made no reference to the documentary evidence filed in support of the applicant, namely the Amnesty International reports.
- Evidence: `reasoning_application` cue `therefore` at chunk `4859254` offsets `87-96`; context: [5] Moreover, the events as described by the applicant may have seemed implausible and therefore not credible to the Refugee Division, but as counsel for the applicant points out "Canadian paradigms do not apply in India".
- Evidence: `reasoning_application` cue `because` at chunk `4859255` offsets `143-150`; context: [10] The applicant alleged that the Bulgarian police and civic officials were trying to evict him and his family from their apartment in Sofia because they were Roma.

#### 18139:2:subtheme:2 · paragraphs 15-18

- Raw key terms: `applicant's, page, tribunal, added, claimant, emphasis, family, roma`
- Display key terms: `applicant's, page, added, emphasis, family, roma`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: applicant's, page, added, emphasis, family, roma Application context: [11] Despite this account, the tribunal concluded that the applicant's testimony was not credible in its entirety because the tribunal perceived his story to be implausible. | The applicant testified that the officials sought to evict him because his family was Roma, and, as shall be seen, there was evidence to support this claim. Evidence spans paragraphs 15-18. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4859256` offsets `352-360`; context: For example, regarding the applicant's testimony that he was being pressured to sign a form which would terminate his apartment lease, the tribunal asks the following rhetorical question at page 11:
.
- Evidence: `evidence_fact` cue `testimony` at chunk `4859256` offsets `71-80`; context: [11] Despite this account, the tribunal concluded that the applicant's testimony was not credible in its entirety because the tribunal perceived his story to be implausible.
- Evidence: `reasoning_application` cue `because` at chunk `4859256` offsets `114-121`; context: [11] Despite this account, the tribunal concluded that the applicant's testimony was not credible in its entirety because the tribunal perceived his story to be implausible.
- Evidence: `evidence_fact` cue `evidence` at chunk `4859258` offsets `275-283`; context: The applicant testified that the officials sought to evict him because his family was Roma, and, as shall be seen, there was evidence to support this claim.
- Evidence: `reasoning_application` cue `because` at chunk `4859258` offsets `213-220`; context: The applicant testified that the officials sought to evict him because his family was Roma, and, as shall be seen, there was evidence to support this claim.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `4859258` offsets `626-632`; context: One cannot understand how the tribunal expects the applicant to explain logically the illogical actions of the authorities.
- Evidence: `evidence_fact` cue `testimony` at chunk `4859259` offsets `37-46`; context: [14] After rejecting the applicant's testimony, the tribunal offers its own version of events at page 12:
The panel believes that the most reasonable explanation is that the seeds of the claimant's conflict probably had their origin in a deteriorating mental condition on the part of the claimant's mother that, in turn, caused her to become a danger to herself and to her neighbours.

#### Section text

[5] Questions of credibility are within the jurisdiction of the tribunal as the trier of fact in respect of Convention refugee claims, and a reviewing court should be hesitant in interfering. However, the Court has a duty to interfere when findings of credibility are patently unreasonable, or when they are made based on erroneous findings of fact made in a perverse or capricious manner without regard for the material before it. For the following reasons, this Court finds that the intervention is warranted here.
Presumption of Truth and Plausibility

[6] The tribunal adverts to the principle from Maldonado v. M.E.I., [1980] 2 F.C 302 (C.A.) at 305, that when a refugee claimant swears to the truth of certain allegations, a presumption is created that those allegations are true unless there are reasons to doubt their truthfulness. But the tribunal does not apply the Maldonado principle to this applicant, and repeatedly disregards his testimony, holding that much of it appears to it to be implausible. Additionally, the tribunal often substitutes its own version of events without evidence to support its conclusions.

[7] A tribunal may make adverse findings of credibility based on the implausibility of an applicant's story provided the inferences drawn can be reasonably said to exist. However, plausibility findings should be made only in the clearest of cases, i.e., if the facts as presented are outside the realm of what could reasonably be expected, or where the documentary evidence demonstrates that the events could not have happened in the manner asserted by the claimant. A tribunal must be careful when rendering a decision based on a lack of plausibility because refugee claimants come from diverse cultures, and actions which appear implausible when judged from Canadian standards might be plausible when considered from within the claimant's milieu. [see L. Waldman, Immigration Law and Practice (Markham, ON: Butterworths, 1992) at 8.22]

[8] In Leung v. M.E.I. (1994), 81 F.T.R. 303 (T.D.), Associate Chief Justice Jerome stated at page 307:

[14] ...Nevertheless, the Board is under a very clear duty to justify its credibility findings with specific and clear reference to the evidence.

[15] This duty becomes particularly important in cases such as this one where the Board has based its non-credibility finding on perceived "implausibilities" in the claimants' stories rather than on internal inconsistencies and contradictions in their narratives or their demeanour while testifying. Findings of implausibility are inherently subjective assessments which are largely dependant on the individual Board member's perceptions of what constitutes rational behaviour. The appropriateness of a particular finding can therefore only be assessed if the Board's decision clearly identifies all of the facts which form the basis for their conclusions. The Board will therefore err when it fails to refer to relevant evidence which could potentially refute their conclusions of implausibility...
(emphasis added)

[9] In Bains v. M.E.I. (1993), 63 F.T.R. 312 (T.D.) at 314, Mr. Justice Cullen quashed a decision of the tribunal after concluding that it erred because its plausibility findings were made without referring to the documentary evidence, and because they were made based on Canadian paradigms:

[4]... However, in making a finding of what was plausible or implausible the Refugee Division made no reference to the documentary evidence filed in support of the applicant, namely the Amnesty International reports. According to the reports, the events described by the applicant were not an unusual occurrence and constant harassment of members or former members of Akali Dal was the norm, not the exception. Therefore, in my view, the failure to comment on the evidence filed, either in a negative or positive manner, seriously weakened the Refugee Division's decision and conclusions. Further, the applicant's contention is wholly consistent with the documentary evidence filed and is probably the only source of evidence sustaining the applicant's case; or is the only clue to determining if the applicant's evidence is plausible. This documentary evidence was the only gauge available regarding the conduct of authorities in Indian vis-à-vis Sikhs and the reports referred to these occurrences as "routine".

[5] Moreover, the events as described by the applicant may have seemed implausible and therefore not credible to the Refugee Division, but as counsel for the applicant points out "Canadian paradigms do not apply in India". Torture, unhappily, is real, as is exploitation and revenge, often resulting in killings.
(emphasis added)

[10] The applicant alleged that the Bulgarian police and civic officials were trying to evict him and his family from their apartment in Sofia because they were Roma. He testified that he was unwilling to leave his apartment because he and his family had previously been evicted and had waited four years to secure new accommodations. The applicant testified that in the attempt to evict him, his mother was improperly incarcerated in a mental asylum where she died, and that he was abducted, savagely beaten, jailed without legal authority, and pulled back from a work assignment abroad in Russia. Further, he stated that his apartment was rigorously searched, and that his family were repeatedly interrogated while his lawyer's efforts to secure justice were brushed aside. Throughout this campaign, there was a continuing effort to compel the applicant to sign a statement voluntarily relinquishing his lodgings, while a parallel effort was underway to seize copies of all of the applicant's complaints to various government officials.

[11] Despite this account, the tribunal concluded that the applicant's testimony was not credible in its entirety because the tribunal perceived his story to be implausible. For example, regarding the applicant's testimony that he was being pressured to sign a form which would terminate his apartment lease, the tribunal asks the following rhetorical question at page 11:
...Why would a regime that was so arbitrary and lawless in its basic character so as to repeatedly beat and abduct the claimant, be fastidious about having him sign an apartment release, or ask him to fill and complete his own summonses and subpoenas? This makes no sense at all...
(emphasis added)
Was that tribunal falsely applying Canadian paradigms?

[12] And at page 12, regarding the repeated searches of the applicant's home, the tribunal continues:
...This makes no sense at all. Nor does the alleged house raid over Easter 1996 in order to seize copies of letters which had already been sent to the various ministers and departments in the Bulgarian government. After all, the claimant was not in possession of any classified or private information, nor was he privy to secrets, which if made public, would constitute embarrassing revelations for the State. The only papers he possessed consisted of copies of his own correspondence. When he was asked why the Bulgarian authorities would go to such lengths to create an appearance of legality around efforts to evict him, he said that if they did not proceed cautiously in their eviction, they might find themselves "facing a Roma revolt." He added that he was in touch with a Roma MP named Manush Romanov and had taken steps to retain a lawyer. These comments, implying as they do that the Bulgarian government was nervous about antagonizing the Roma community are completely at odds with a multitude of other statements made by the claimant indicating the Bulgarian state was completely indifferent to the situation of the Roma community and cared not a fig for its general welfare. As well the observation, if ingested at face value, borders on the inherently absurd - if the Bulgarian State wished to appear scrupulously ‘legal' about an eviction order for fear of Roma anger, why would the same state abduct and brutalize the claimant and his family? Does a "legal" eviction make for better political "optics" than kidnapping, terror, and physical brutality?
(emphasis added)

[13] Throughout this decision, the tribunal asks the applicant to explain the actions of the authorities, and then categorically rejects his answers. The applicant testified that the officials sought to evict him because his family was Roma, and, as shall be seen, there was evidence to support this claim. What more could he say? The tribunal itself reviewed the entrenched discrimination and persecution against the Roma in Bulgaria starting at page 16 of the decision, yet rejected the applicant's explanation that he was being pressured to sign a document which would force him from his apartment because he was Roma. One cannot understand how the tribunal expects the applicant to explain logically the illogical actions of the authorities. It was not implausible that the authorities needed his signature to terminate the lease, but, without evidence to support its findings, the tribunal was in no position to contradict the applicant's testimony.

[14] After rejecting the applicant's testimony, the tribunal offers its own version of events at page 12:
The panel believes that the most reasonable explanation is that the seeds of the claimant's conflict probably had their origin in a deteriorating mental condition on the part of the claimant's mother that, in turn, caused her to become a danger to herself and to her neighbours. This would explain the "fire" episode that apparently led to her hospitalization. In the panel's view, it beggars belief that a neighbour would have deliberately started a blaze in order to wrongly [sic] blame the claimant's mother. Why would anyone risk their [sic]own life [sic] or their neighbours'lives in such a mad endeavour? Why would they need to, if prejudice against a Roma family, in the complex was so strong that eviction could move forward on that basis alone? Further, it seems probable to the panel that intemperate (possibly defamatory) accusations by the claimant concerning his mother's hospitalization and death, expressed in strongly-worded letters to Ministers, set the stage for further conflicts with neighbours and civic officials.
(emphasis added)

## 18139:3 · paragraphs 19-58

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `7129337c683a6d8f170c4d7c12a9fb0b5bcdbee6acc53a0abe0fc7a2abcffbb7`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 18139:3:subtheme:1 · paragraphs 19-21

- Raw key terms: `applicant's, evidence, tribunal, applicant, authorities, blame, family, finally`
- Display key terms: `applicant's, authorities, blame, family, finally`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: applicant's, authorities, blame, family, finally Application context: Firstly, the tribunal posits a theory that the applicant's conflict with the housing authorities started because of his mother's mental condition which caused her to become a danger to herself and to her neighbours. | [17] The tribunal did not apply the principle elaborated in Maldonado, supra, to this applicant. Evidence spans paragraphs 19-21. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `evidence` at chunk `4859260` offsets `278-286`; context: There was no evidence to support this conclusion, and as such, it is pure speculation by the tribunal.
- Evidence: `reasoning_application` cue `because` at chunk `4859260` offsets `154-161`; context: Firstly, the tribunal posits a theory that the applicant's conflict with the housing authorities started because of his mother's mental condition which caused her to become a danger to herself and to her neighbours.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `4859260` offsets `481-487`; context: Secondly, the tribunal finds that the applicant's story is implausible when it states, without evidence, that it cannot believe that a neighbour would deliberately start a blaze wrongly to blame the applicant's mother.
- Evidence: `issue` cue `whether` at chunk `4859261` offsets `729-736`; context: After stating that his family were co-defendants and victims of persecution along with the claimant and that all the persecution had "shifted to the shoulders of my son," the claimant was asked whether any effort had been made to evict them since his departure.
- Evidence: `evidence_fact` cue `evidence` at chunk `4859261` offsets `64-72`; context: [16] The tribunal questions the plausibility of the applicant's evidence once again at page 14 when it asks him to explain the actions of the authorities who interrogated his children, and once again rejects his answer:
He was then asked what he felt the authorities sought to achieve by interrogating his daughter and he said that the prosecutor insisted she "sign a paper.
- Evidence: `evidence_fact` cue `testimony` at chunk `4859262` offsets `153-162`; context: The tribunal wrongly rejected the applicant's plausible testimony, and improperly injected its own version of events without evidence to support its conclusions.
- Evidence: `reasoning_application` cue `apply` at chunk `4859262` offsets `26-31`; context: [17] The tribunal did not apply the principle elaborated in Maldonado, supra, to this applicant.

#### 18139:3:subtheme:2 · paragraphs 22-24

- Raw key terms: `applicant's, claimant, page, stated, tribunal, added, card, claimant's`
- Display key terms: `applicant's, page, stated, added, card, claimant's`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: applicant's, page, stated, added, card, claimant's Rule/authority context: To this testimony, the tribunal stated the following at page 14: The panel pointed out that the claimant's son was actually 25 in 1996 and therefore not a minor under the law. Application context: To this testimony, the tribunal stated the following at page 14: The panel pointed out that the claimant's son was actually 25 in 1996 and therefore not a minor under the law. Evidence spans paragraphs 22-24. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4859263` offsets `665-673`; context: The tribunal stated the following regarding this evidence:
The panel notes that there is no reference at all to the ethnicity of the claimant or his family members on the card in question, which was issued on April 26, 1993, nor are the claimant's mother or his (then 22 year-old son) shown as residents, although the claimant testified that all were then part of his household.
- Evidence: `evidence_fact` cue `evidence` at chunk `4859263` offsets `69-77`; context: [18] When discussing the applicant's credibility, the tribunal omits evidence which supports his claim.
- Evidence: `counterargument_limitation` cue `although` at chunk `4859263` offsets `791-799`; context: The tribunal stated the following regarding this evidence:
The panel notes that there is no reference at all to the ethnicity of the claimant or his family members on the card in question, which was issued on April 26, 1993, nor are the claimant's mother or his (then 22 year-old son) shown as residents, although the claimant testified that all were then part of his household.
- Evidence: `evidence_fact` cue `Record` at chunk `4859264` offsets `255-261`; context: In fact, the address card clearly indicates the words "Roma Family" in the top left hand corner (see page 173 of the Tribunal Record).
- Evidence: `evidence_fact` cue `evidence` at chunk `4859265` offsets `57-65`; context: [20] The tribunal then mis-characterizes the applicant's evidence regarding his children's interrogation.
- Evidence: `governing_rule` cue `under` at chunk `4859265` offsets `529-534`; context: To this testimony, the tribunal stated the following at page 14:
The panel pointed out that the claimant's son was actually 25 in 1996 and therefore not a minor under the law.
- Evidence: `reasoning_application` cue `therefore` at chunk `4859265` offsets `507-516`; context: To this testimony, the tribunal stated the following at page 14:
The panel pointed out that the claimant's son was actually 25 in 1996 and therefore not a minor under the law.

#### 18139:3:subtheme:3 · paragraphs 25-30

- Raw key terms: `tribunal, applicant, demeanour, evidence, manner, testimony, applicant's, credible`
- Display key terms: `demeanour, manner, testimony, applicant's, credible`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: demeanour, manner, testimony, applicant's, credible Application context: A lawyer who was supposed to defend, to appear and to defend my children, because they are minor, and there is a law- there is a law, just like my daughter is a minor, there must be lawyer or the mother must be present t | [22] Therefore, the tribunal mis-characterizes the evidence twice: firstly, the applicant did in fact respond, and secondly, he clearly indicated that he was discussing his daughter, who was a minor at the time of the in Evidence spans paragraphs 25-30. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4859266` offsets `121-129`; context: [21] However, the following exchange is recorded at page 29 of the transcript of proceedings:
Presiding Member: Sir, the question was: what was the lawyer going to do for your children?
- Evidence: `reasoning_application` cue `because` at chunk `4859266` offsets `292-299`; context: A lawyer who was supposed to defend, to appear and to defend my children, because they are minor, and there is a law- there is a law, just like my daughter is a minor, there must be lawyer or the mother must be present too or -
.
- Evidence: `evidence_fact` cue `evidence` at chunk `4859267` offsets `51-59`; context: [22] Therefore, the tribunal mis-characterizes the evidence twice: firstly, the applicant did in fact respond, and secondly, he clearly indicated that he was discussing his daughter, who was a minor at the time of the interrogation.
- Evidence: `reasoning_application` cue `Therefore` at chunk `4859267` offsets `5-14`; context: [22] Therefore, the tribunal mis-characterizes the evidence twice: firstly, the applicant did in fact respond, and secondly, he clearly indicated that he was discussing his daughter, who was a minor at the time of the interrogation.
- Evidence: `evidence_fact` cue `testimony` at chunk `4859268` offsets `322-331`; context: He tended to shout to emphasize points; often rambled, had to be frequently cautioned about "out-running"the interpreter, and much of his oral testimony consisted of wooden, declamatory rhetoric displaying a rehearsed and unspontaneous character.
- Evidence: `evidence_fact` cue `evidence` at chunk `4859269` offsets `41-49`; context: [24] In assessing the credibility of the evidence, a tribunal can evaluate the general demeanour of the applicant as he or she is testifying.
- Evidence: `counterargument_limitation` cue `However` at chunk `4859269` offsets `350-357`; context: However, problems may arise in interpreting the demeanour of refugee claimants from different cultural backgrounds.
- Evidence: `evidence_fact` cue `testimony` at chunk `4859270` offsets `667-676`; context: In assessing the manner in which he delivered his answers, the tribunal stated that the applicant's testimony was wooden, declamatory, rehearsed and unspontaneous.
- Evidence: `counterargument_limitation` cue `Although` at chunk `4859270` offsets `731-739`; context: Although these epithets connote dishonesty, the tribunal directly contradicted itself when it observed that the applicant's testimony was rambling, off-centre, and evasive.
- Evidence: `evidence_fact` cue `evidence` at chunk `4859271` offsets `347-355`; context: [26] The tribunal's conclusion that the applicant is not credible is highly questionable for several reasons: the tribunal does not apply the presumption of truthfulness from Maldonado, supra to this applicant; the tribunal makes findings of implausibility which are unreasonable; the tribunal eagerly substitutes its own version of facts without evidence to support its conclusions; the tribunal made errors of fact or mis-characterized evidence; and the tribunal draws negative inferences regarding the applicant, despite its own contradictory observations regarding his demeanour.
- Evidence: `reasoning_application` cue `apply` at chunk `4859271` offsets `132-137`; context: [26] The tribunal's conclusion that the applicant is not credible is highly questionable for several reasons: the tribunal does not apply the presumption of truthfulness from Maldonado, supra to this applicant; the tribunal makes findings of implausibility which are unreasonable; the tribunal eagerly substitutes its own version of facts without evidence to support its conclusions; the tribunal made errors of fact or mis-characterized evidence; and the tribunal draws negative inferences regarding the applicant, despite its own contradictory observations regarding his demeanour.

#### 18139:3:subtheme:4 · paragraphs 31-34

- Raw key terms: `documents, reason, tribunal, another, decision, difficult, discussed, ethnicity`
- Display key terms: `documents, reason, another, difficult, discussed, ethnicity`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: documents, reason, another, difficult, discussed, ethnicity Application context: Despite that the tribunal is not obliged to refer in its reasons to all of the evidence which was before it, "this principle does not apply to a failure to make reference to a case-specific document that is evidence dire | Finally, the tribunal rejected the photocopied documents because they were "problematical for one reason or another. Evidence spans paragraphs 31-34. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4859272` offsets `483-488`; context: Despite that the tribunal is not obliged to refer in its reasons to all of the evidence which was before it, "this principle does not apply to a failure to make reference to a case-specific document that is evidence directly relevant to the central issue addressed in the tribunal's decision.
- Evidence: `evidence_fact` cue `evidence` at chunk `4859272` offsets `92-100`; context: [27] Several problems arose from the manner in which the tribunal evaluated the documentary evidence regarding the applicant's ethnicity.
- Evidence: `reasoning_application` cue `apply` at chunk `4859272` offsets `368-373`; context: Despite that the tribunal is not obliged to refer in its reasons to all of the evidence which was before it, "this principle does not apply to a failure to make reference to a case-specific document that is evidence directly relevant to the central issue addressed in the tribunal's decision.
- Evidence: `counterargument_limitation` cue `However` at chunk `4859273` offsets `407-414`; context: However, the tribunal does not explain how the RCMP's findings affected its decision, if at all.
- Evidence: `counterargument_limitation` cue `However` at chunk `4859274` offsets `81-88`; context: [29] A second possible reason for omitting the documents is discussed at page 6:
However, assessing the claimant's allegation that he is Roma or "Gypsy" and determining how potential persecutors might arrive at that same conclusion proved difficult.
- Evidence: `evidence_fact` cue `evidence` at chunk `4859275` offsets `410-418`; context: " This casual assessment is difficult to accept given the importance of the evidence to the claim, and given the tribunal's material error regarding the apartment address card.
- Evidence: `reasoning_application` cue `because` at chunk `4859275` offsets `275-282`; context: Finally, the tribunal rejected the photocopied documents because they were "problematical for one reason or another.

#### 18139:3:subtheme:5 · paragraphs 35-42

- Raw key terms: `tribunal, roma, applicant, page, added, asked, bulgaria, claimant`
- Display key terms: `roma, page, added, asked, bulgaria`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: roma, page, added, asked, bulgaria Application context: The tribunal continues at page 9: The panel was curious as to why the claimant would have applied to obtain a baptism certificate in 1985. | " The tribunal analyzed this letter and accorded it low probative value because the applicant was not personally known to the mayor. Evidence spans paragraphs 35-42. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4859276` offsets `307-315`; context: The certificate in question describes both parents of the claimant as ‘Roma.
- Evidence: `evidence_fact` cue `record` at chunk `4859276` offsets `239-245`; context: The first was a photocopy of a baptismal certificate issued on April 18th, 1985, in Plovdiv, Bulgaria purporting to record the claimant's baptism on August 9, 1948.
- Evidence: `issue` cue `whether` at chunk `4859277` offsets `367-374`; context: The tribunal continued at page 8:
The claimant was also asked whether he had ever possessed a birth certificate issued by district authorities and he replied that he did not have such a document and added that such registrations were ‘purely discretionary' on the part of parents.
- Evidence: `evidence_fact` cue `evidence` at chunk `4859277` offsets `52-60`; context: [32] Once again, the tribunal mis-characterizes the evidence.
- Evidence: `counterargument_limitation` cue `but` at chunk `4859277` offsets `221-224`; context: As recorded at page 15 of the transcript of the proceedings, the applicant did not state that he did not know of the whereabouts of the baptismal certificate, but rather that his parents had lost the original and that he had needed a new one.
- Evidence: `reasoning_application` cue `applied` at chunk `4859278` offsets `357-364`; context: The tribunal continues at page 9:
The panel was curious as to why the claimant would have applied to obtain a baptism certificate in 1985.
- Evidence: `reasoning_application` cue `because` at chunk `4859280` offsets `298-305`; context: " The tribunal analyzed this letter and accorded it low probative value because the applicant was not personally known to the mayor.
- Evidence: `counterargument_limitation` cue `however` at chunk `4859282` offsets `972-979`; context: ' The claimant said his eyes were actually green, that many Bulgarian Roma had green eyes, and that as a youth he had been darker; however, he also acknowledged that "other Bulgarian Roma were dark.
- Evidence: `reasoning_application` cue `because` at chunk `4859283` offsets `284-291`; context: Further, the tribunal admits to having no experience regarding the Bulgarian Roma, yet is quick to dismiss his claim in part because of his appearance.

#### 18139:3:subtheme:6 · paragraphs 43-44

- Raw key terms: `assessment, basis, dark, ethnicity, particular, people, person, pluharova`
- Display key terms: `assessment, basis, dark, ethnicity, particular, people, person, pluharova`
- Argument roles: `counterargument_limitation, issue`
- Explanation: Observed roles: counterargument_limitation, issue Display terms: assessment, basis, dark, ethnicity, particular, people, person, pluharova Evidence spans paragraphs 43-44. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4859284` offsets `266-273`; context: It is inherently dangerous for Board members to base a finding on whether people in another country would regard a claimant as of particular ethnicity solely on the basis of the members' observation of the person concerned.
- Evidence: `counterargument_limitation` cue `However` at chunk `4859285` offsets `157-164`; context: However, since Ms.

#### 18139:3:subtheme:7 · paragraphs 45-49

- Raw key terms: `roma, added, applicant, bulgarians, emphasis, page, risk, tribunal`
- Display key terms: `roma, added, bulgarians, emphasis, page, risk`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: roma, added, bulgarians, emphasis, page, risk Application context: 689 at 747 that it is appropriate when considering claims to refugee status based on any of the grounds set out in the definition also to consider the perspective of the persecutor, because that is the perspective which  | [40] And at page 8: The panel concludes that the claimant would not be perceived to be Roma by fellow Bulgarians who possessed no specific knowledge of his alleged family antecedents. Evidence spans paragraphs 45-49. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4859286` offsets `485-492`; context: In discussing the risk to the applicant based on his appearance, the tribunal stated at page 7:
The panel asked the claimant whether his physical appearance would enable other Bulgarians to conclude he was Roma were he to appear on a street in Sofia.
- Evidence: `reasoning_application` cue `because` at chunk `4859286` offsets `276-283`; context: 689 at 747 that it is appropriate when considering claims to refugee status based on any of the grounds set out in the definition also to consider the perspective of the persecutor, because that is the perspective which is determinative in inciting the persecution.
- Evidence: `counterargument_limitation` cue `but` at chunk `4859286` offsets `709-712`; context: He said that other Bulgarians would know he was Roma because of his "bright picturesque clothing" but he later acknowledged that if he wore regular clothing it would be difficult to say he was Roma.
- Evidence: `reasoning_application` cue `concludes` at chunk `4859287` offsets `30-39`; context: [40] And at page 8:
The panel concludes that the claimant would not be perceived to be Roma by fellow Bulgarians who possessed no specific knowledge of his alleged family antecedents.
- Evidence: `reasoning_application` cue `therefore` at chunk `4859288` offsets `464-473`; context: His risk of persecution is therefore effectively at the level of "mere possibility".
- Evidence: `counterargument_limitation` cue `However` at chunk `4859288` offsets `270-277`; context: However, in a large center like Sofia it is safe to say that someone with the claimant's attributes and background would blend seamlessly into the Bulgarian majority.
- Evidence: `evidence_fact` cue `determined that` at chunk `4859289` offsets `249-264`; context: That they have already determined that he is Roma belies the tribunal's assumption that his risk is a mere possibility.
- Evidence: `reasoning_application` cue `because` at chunk `4859289` offsets `56-63`; context: [42] The tribunal's analysis that the applicant is safe because other Bulgarians would not recognize him as being Roma is incomplete.

#### 18139:3:subtheme:8 · paragraphs 50-54

- Raw key terms: `tribunal, applicant, applicant's, canada, states, united, court, delay`
- Display key terms: `applicant's, states, united, delay`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: applicant's, states, united, delay Position/evidence statements: Once in the United States, he doubtless heard about the movement of Czech Roma to Canada - a phenomenon that attracted world-wide publicity - and decided to test the waters with a claim built upon the same foundation. Rule/authority context: Those comments may be truthful in the narrow sense that they were made but, equally, they are not redolent of the behaviour of a person acting under a genuine and driving fear of persecution. Application context: He alleged in his PIF that he went to United States, though always intending to go to Canada for asylum, solely because there is no Canadian Embassy in Sofia and he could not obtain a Canadian visitor visa there. Evidence spans paragraphs 50-54. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4859291` offsets `888-896`; context: The claimant's response to this question was fuzzy and unclear.
- Evidence: `evidence_fact` cue `testimony` at chunk `4859291` offsets `445-454`; context: In his oral testimony, by contrast, he said that he went United States because he had contacts in the construction field, who were able to secure an American visa for a fee of $2,500.
- Evidence: `governing_rule` cue `under` at chunk `4859291` offsets `1205-1210`; context: Those comments may be truthful in the narrow sense that they were made but, equally, they are not redolent of the behaviour of a person acting under a genuine and driving fear of persecution.
- Evidence: `reasoning_application` cue `because` at chunk `4859291` offsets `332-339`; context: He alleged in his PIF that he went to United States, though always intending to go to Canada for asylum, solely because there is no Canadian Embassy in Sofia and he could not obtain a Canadian visitor visa there.
- Evidence: `party_position` cue `claim` at chunk `4859293` offsets `456-461`; context: Once in the United States, he doubtless heard about the movement of Czech Roma to Canada - a phenomenon that attracted world-wide publicity - and decided to test the waters with a claim built upon the same foundation.
- Evidence: `evidence_fact` cue `evidence` at chunk `4859293` offsets `98-106`; context: [46] On page 16, the tribunal once again attempts to explain the actions of the applicant without evidence:
The panel believes that the claimant went to the United States intending to live and work there illegally for reasons not attached to fear but of economic advancement.
- Evidence: `counterargument_limitation` cue `but` at chunk `4859293` offsets `247-250`; context: [46] On page 16, the tribunal once again attempts to explain the actions of the applicant without evidence:
The panel believes that the claimant went to the United States intending to live and work there illegally for reasons not attached to fear but of economic advancement.
- Evidence: `evidence_fact` cue `evidence` at chunk `4859294` offsets `190-198`; context: The tribunal once again speculates without evidence by stating that the applicant intended to live and work illegally in the United States.
- Evidence: `counterargument_limitation` cue `Although` at chunk `4859295` offsets `159-167`; context: Although one cannot agree with the assertion that a negative description of an applicant's demeanour, per se, constitutes a reasonable apprehension of bias, this Court infers that in this instance it is merely one aspect of a pattern which raises the Court's reasonable apprehension of the tribunal's probable bias against this applicant.

#### 18139:3:subtheme:9 · paragraphs 55-57

- Raw key terms: `conclusion, tribunal, applicant, applicant's, apprehension, bias, costs, court's`
- Display key terms: `conclusion, applicant's, apprehension, bias, costs, court's`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: conclusion, applicant's, apprehension, bias, costs, court's Rule/authority context: [51] Given the Court's conclusion regarding the conduct of the tribunal in this matter, the Court finds that there are special reasons for the Minister to bear the costs of this application under Rule 22 of the Federal C Application context: [49] The test for a reasonable apprehension of bias is whether an informed person, viewing the matter realistically and practically, and having thought the matter through would conclude that there was a reasonable appreh Evidence spans paragraphs 55-57. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4859296` offsets `55-62`; context: [49] The test for a reasonable apprehension of bias is whether an informed person, viewing the matter realistically and practically, and having thought the matter through would conclude that there was a reasonable apprehension of bias on the part of the tribunal members [see Committee for Justice & Liberty v.
- Evidence: `evidence_fact` cue `evidence` at chunk `4859296` offsets `930-938`; context: The tribunal's speculation, without evidence, regarding the events surrounding his mother's commitment to a mental hospital;
f.
- Evidence: `reasoning_application` cue `conclude` at chunk `4859296` offsets `177-185`; context: [49] The test for a reasonable apprehension of bias is whether an informed person, viewing the matter realistically and practically, and having thought the matter through would conclude that there was a reasonable apprehension of bias on the part of the tribunal members [see Committee for Justice & Liberty v.
- Evidence: `evidence_fact` cue `testimony` at chunk `4859297` offsets `205-214`; context: The tribunal's steadfast refusal to accept the applicant's testimony, combined with its errors in reviewing the documentary evidence which appeared to favour the applicant, and its insistence on substituting its own version of events without evidence lead to the conclusion that the applicant did not have a fair chance to obtain Convention refugee status.
- Evidence: `governing_rule` cue `under` at chunk `4859298` offsets `190-195`; context: [51] Given the Court's conclusion regarding the conduct of the tribunal in this matter, the Court finds that there are special reasons for the Minister to bear the costs of this application under Rule 22 of the Federal Court Immigration Rules, 1993.

#### 18139:3:subtheme:10 · paragraphs 58-58

- Raw key terms: `agreed, allowed, applicant's, application, back, case, certified, circumstances`
- Display key terms: `agreed, allowed, applicant's, back, case, certified, circumstances`
- Argument roles: `disposition, issue`
- Explanation: Observed roles: disposition, issue Display terms: agreed, allowed, applicant's, back, case, certified, circumstances Operative outcome context: [52] The application for judicial review is allowed, and the matter is remitted back to a differently constituted panel of the Convention Refugee Determination Division. Evidence spans paragraphs 58-58. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4859299` offsets `303-311`; context: Both counsel agreed that there is no determinative question to be certified in the circumstances of this case.
- Evidence: `disposition` cue `allowed` at chunk `4859299` offsets `44-51`; context: [52] The application for judicial review is allowed, and the matter is remitted back to a differently constituted panel of the Convention Refugee Determination Division.

#### Section text

[15] There are three problems with this passage. Firstly, the tribunal posits a theory that the applicant's conflict with the housing authorities started because of his mother's mental condition which caused her to become a danger to herself and to her neighbours. There was no evidence to support this conclusion, and as such, it is pure speculation by the tribunal. Secondly, the tribunal finds that the applicant's story is implausible when it states, without evidence, that it cannot believe that a neighbour would deliberately start a blaze wrongly to blame the applicant's mother. Finally, the tribunal wrongly blames the applicant for his predicament because, in its opinion, his complaints to the authorities regarding his mother's treatment were intemperate and defamatory, and set the stage for further conflict. Was the applicant expected to accept his fate meekly, and let a member of his family be taken away without a word? To blame the applicant here evinces a degree of callousness, and possible bias by the tribunal.

[16] The tribunal questions the plausibility of the applicant's evidence once again at page 14 when it asks him to explain the actions of the authorities who interrogated his children, and once again rejects his answer:
He was then asked what he felt the authorities sought to achieve by interrogating his daughter and he said that the prosecutor insisted she "sign a paper." Did the claimant know what was in the paper? He testified that he did not, neither did his daughter, and that, in any event, they had not really discussed it. After stating that his family were co-defendants and victims of persecution along with the claimant and that all the persecution had "shifted to the shoulders of my son," the claimant was asked whether any effort had been made to evict them since his departure.
(emphasis added)

[17] The tribunal did not apply the principle elaborated in Maldonado, supra, to this applicant. The tribunal wrongly rejected the applicant's plausible testimony, and improperly injected its own version of events without evidence to support its conclusions. Finally, it was perverse for the tribunal to blame the applicant for complaining to officials about forcibly removing his mother from his apartment, thereby implying that he was responsible for his own predicament.
Errors of Fact / Mis-characterization of Evidence

[18] When discussing the applicant's credibility, the tribunal omits evidence which supports his claim. At page 13, the tribunal states that the applicant was asked to explain how his neighbours discovered that he and his family were Roma. The applicant answered that each apartment building contained a central registry where families were required to record their ethnic origins. Counsel for the applicant submitted to the tribunal an extract from the registry on September 24, 1998. The tribunal stated the following regarding this evidence:
The panel notes that there is no reference at all to the ethnicity of the claimant or his family members on the card in question, which was issued on April 26, 1993, nor are the claimant's mother or his (then 22 year-old son) shown as residents, although the claimant testified that all were then part of his household. The panel finds the claimant's allegation that his neighbours discovered his Roma origins by means of the apartment registry not credible.
(emphasis added)

[19] The tribunal erred when it stated that there is no reference to the ethnicity of the claimant or of his family on the card. In fact, the address card clearly indicates the words "Roma Family" in the top left hand corner (see page 173 of the Tribunal Record). Given the importance of the applicant's ethnicity in the eyes of the tribunal, this is a serious omission.

[20] The tribunal then mis-characterizes the applicant's evidence regarding his children's interrogation. He testified that, before his departure from Bulgaria, his minor children had been interrogated by prosecutors, and that neither he nor his lawyer had been permitted to observe the interrogations. He stated that he engaged a lawyer to safeguard their interests. To this testimony, the tribunal stated the following at page 14:
The panel pointed out that the claimant's son was actually 25 in 1996 and therefore not a minor under the law. The claimant made no response to this comment.
(emphasis added)

[21] However, the following exchange is recorded at page 29 of the transcript of proceedings:
Presiding Member: Sir, the question was: what was the lawyer going to do for your children? You told us all this before.
A. A lawyer who was supposed to defend, to appear and to defend my children, because they are minor, and there is a law- there is a law, just like my daughter is a minor, there must be lawyer or the mother must be present too or -
...
Presiding Member: I don't want to ask questions during - when you're questioning him, but I must ask. I'm confused. Your son at today's date is 28 years old.
A. Yes.
Presiding Member: He wasn't a minor when any of this was going on.
A. I was talking about my minor daughter.
(emphasis added)

[22] Therefore, the tribunal mis-characterizes the evidence twice: firstly, the applicant did in fact respond, and secondly, he clearly indicated that he was discussing his daughter, who was a minor at the time of the interrogation. The manner in which the tribunal describes the applicant leads the casual reader to infer that he is not credible, despite the fact that it is the tribunal which is mistaken in relating his testimony.
The Applicant's Demeanour

[23] The tribunal evaluated the applicant's demeanour while testifying at page 10 of the decision:
The panel found the witness to be verbose and often overly assertive in manner. He tended to shout to emphasize points; often rambled, had to be frequently cautioned about "out-running"the interpreter, and much of his oral testimony consisted of wooden, declamatory rhetoric displaying a rehearsed and unspontaneous character. At times his answers were prolix in the extreme, off-centre, and evasive. In fairness to the claimant, the panel also sensed that he did seem to have a festering sense of anger that may have had its origins in some form of injustice or what the claimant perceived to be injustice. Given the claimant's voluble and bombastic testimony, the panel found it necessary to discriminate closely between the claimant's perceptions of reality and objective reality when evaluating and weighing his evidence.
(emphasis added)
That it is solely for the tribunal to assess the claimant's testimony is a principle which is sometimes stated with almost religious zeal

[24] In assessing the credibility of the evidence, a tribunal can evaluate the general demeanour of the applicant as he or she is testifying. This involves assessing the manner in which the witness replies to questions, his or her facial expressions, tone of voice, physical movements, general integrity and intelligence, and powers of recollection. However, problems may arise in interpreting the demeanour of refugee claimants from different cultural backgrounds. Moreover, persons who have suffered persecution may experience problems in relating their testimony.

[25] The tribunal wrongly put the applicant's personality on trial. For example, the tribunal noted that the applicant was overly assertive, bombastic, and that he shouted to emphasize points. How does being overly assertive permit the tribunal to draw a negative inference about credibility? In assessing his speaking style, the tribunal stated that the applicant was verbose, voluble, prolix and that the interpreter could not keep up with him. Again, how does the length of the applicant's answers permit the tribunal to state that the applicant was not credible? In assessing the manner in which he delivered his answers, the tribunal stated that the applicant's testimony was wooden, declamatory, rehearsed and unspontaneous. Although these epithets connote dishonesty, the tribunal directly contradicted itself when it observed that the applicant's testimony was rambling, off-centre, and evasive. How can the applicant be simultaneously wooden yet bombastic, or rehearsed yet rambling? The tribunal appears to have held the applicant's personality against him, forgetting that claimants from different cultural backgrounds may act and express themselves differently.
Summary: Credibility

[26] The tribunal's conclusion that the applicant is not credible is highly questionable for several reasons: the tribunal does not apply the presumption of truthfulness from Maldonado, supra to this applicant; the tribunal makes findings of implausibility which are unreasonable; the tribunal eagerly substitutes its own version of facts without evidence to support its conclusions; the tribunal made errors of fact or mis-characterized evidence; and the tribunal draws negative inferences regarding the applicant, despite its own contradictory observations regarding his demeanour.
5. Ethnicity
Documents

[27] Several problems arose from the manner in which the tribunal evaluated the documentary evidence regarding the applicant's ethnicity. The most striking one is the paucity of documents which were actually reviewed by the tribunal. Despite that the tribunal is not obliged to refer in its reasons to all of the evidence which was before it, "this principle does not apply to a failure to make reference to a case-specific document that is evidence directly relevant to the central issue addressed in the tribunal's decision." [see Atwal v. Canada (Secretary of State) (1994), 82 F.T.R. 73 (T.D.) at 75]. This Court finds that the tribunal did not have regard to the totality of the evidence in the record upon reaching its conclusions.

[28] The tribunal does not adequately explain why it omitted documents from review. One possible reason is discussed at page 1 of the decision where the tribunal states that it received post-hearing submissions from the applicant which appeared to display handwriting anomalies. After notifying counsel, the documents were forwarded for forensic analysis to the RCMP. The RCMP's findings were inconclusive. However, the tribunal does not explain how the RCMP's findings affected its decision, if at all.

[29] A second possible reason for omitting the documents is discussed at page 6:
However, assessing the claimant's allegation that he is Roma or "Gypsy" and determining how potential persecutors might arrive at that same conclusion proved difficult. None of the documents submitted by the claimant that also exhibit security features mention [sic] ethnic group. Those provided by the claimant in photocopy form that do refer to ethnicity are problematical for one reason or another...
(emphasis added)

[30] The tribunal does not explain why it separated the documents into two categories: those with security features, and those without security features. Nor does it explain to which security features it is referring. Finally, the tribunal rejected the photocopied documents because they were "problematical for one reason or another." This casual assessment is difficult to accept given the importance of the evidence to the claim, and given the tribunal's material error regarding the apartment address card.

[31] One of the documents which was reviewed was the applicant's baptismal certificate. The tribunal states at page 8:
... The first was a photocopy of a baptismal certificate issued on April 18th, 1985, in Plovdiv, Bulgaria purporting to record the claimant's baptism on August 9, 1948. The certificate in question describes both parents of the claimant as ‘Roma.' The claimant was asked whether he had possessed an earlier certificate issued at the actual time of baptism, and he indicated that such a certificate had once existed but that he did not know its current whereabouts.
(emphasis added)

[32] Once again, the tribunal mis-characterizes the evidence. As recorded at page 15 of the transcript of the proceedings, the applicant did not state that he did not know of the whereabouts of the baptismal certificate, but rather that his parents had lost the original and that he had needed a new one. The tribunal continued at page 8:
The claimant was also asked whether he had ever possessed a birth certificate issued by district authorities and he replied that he did not have such a document and added that such registrations were ‘purely discretionary' on the part of parents. Later on in his evidence he seemed to indicate that district registrations were mandatory for all, but somehow this process had not been followed in his own case. The panel has no precise information surrounding birth registration requirements in Bulgaria during the period in which the claimant was born, but notes from its experience with other claims that it would be a decided departure from normal communist government practice to permit secular birth registrations to be made on a ‘discretionary'basis. This was particularly the case during the period in question as church attendance and church record-keeping at that time were both proscribed, according to the claimant.
(emphasis added)

[33] Once again, the tribunal engages in speculation: it admits that it has no precise information surrounding birth registration requirements in Bulgaria during the period in which the claimant was born, yet it nonetheless impugns the applicant's version of events. The tribunal continues at page 9:
The panel was curious as to why the claimant would have applied to obtain a baptism certificate in 1985. At that point, the communist regime was still in place and any connections with the church were politically dangerous to exhibit. When asked why he obtained such a certificate, the claimant said (after much hesitation) that he "needed proof"that he was Roma. This reply made absolutely no sense to the panel given the claimant's overarching allegation that all his problems flowed from his Roma ethnicity.
(emphasis added)

[34] After a thorough review of the transcript of the proceedings, the Court has been unable to locate the specific quote where the applicant states that he "needed proof" that he was Roma. This is curious, given that the tribunal appears to be directly quoting him.

[35] The second document which is reviewed by the tribunal at page 9 is a letter dated January 30, 1997, from the mayor of Kurdzhaly which certified that the applicant was a "Bulgarian citizen of the Roma (Gypsy) ethnic group." The tribunal analyzed this letter and accorded it low probative value because the applicant was not personally known to the mayor.

[36] Of the many documents which were omitted from review is a letter from a former member of Parliament, Mr. Romanov. The letter refers to the applicant in terms of his being a Roma. What is particularly puzzling about this omission is that the tribunal specifically requested this letter at page 42 of the transcript, indicating that it has the most potential value of all of the documents. After specifically asking to see the document, the tribunal does not refer to it in its decision. This document, as well as others which were made available to the tribunal, appear to support the applicant's claim to Convention refugee status, and it was an error to omit it from its analysis without explanation.
The Claimant's Appearance

[37] The tribunal questioned the applicant closely about his physical appearance, and observed that he had a fair complexion and blue eyes rather than the dark-eyed and dark-skinned appearance that is ascribed to the Roma. The tribunal stated the following at page 7 of the decision:
The claimant was asked to react to the panel's observation that he was of fair complexion and had blue eyes. It was further noted that in most other Roma claims which the panel had previously assessed from eastern European countries (other than Bulgaria), claimants had been dark-eyed and dark in colouring, clearly displaying the origins in the Indian subcontinent ascribed to them by linguists and cultural anthropologists. As well information contained in Exhibit 2 states that "Bulgarians have historically considered Gypsies to be ‘dark-skinned people.' The claimant said his eyes were actually green, that many Bulgarian Roma had green eyes, and that as a youth he had been darker; however, he also acknowledged that "other Bulgarian Roma were dark."
(emphasis added)

[38] The tribunal incorrectly remarked that the applicant had blue eyes, and does not appear to accept his assertion that many Bulgarian Roma have green eyes. Further, the tribunal admits to having no experience regarding the Bulgarian Roma, yet is quick to dismiss his claim in part because of his appearance. In Pluhar v. M.C.I. (1999), 174 F.T.R. 153 (T.D.) at 155, Mr. Justice Evans stated the following regarding appearance:

[10] In my opinion the Refugee Division erred in law by effectively basing the decision on its assessment that Ms. Pluharova was not dark skinned, especially since it claimed no relevant "expertise". It is inherently dangerous for Board members to base a finding on whether people in another country would regard a claimant as of particular ethnicity solely on the basis of the members' observation of the person concerned.

[11] There may, of course, be some situations in which it will be quite obvious from a person's appearance that the person is not of a particular ethnicity. However, since Ms. Pluharova had black hair and a "sun tanned"appearance, the panel's "common sense" was an insufficiently reliable basis for the panel's assessment of such a sensitive matter. Skin tone cannot be categorized simply as either "light" or "dark": there is a broad spectrum between these polarities. Racists may be able to identify a person as a member of a minority group by physical characteristics that would not necessarily be apparent to people in other countries.
(emphasis added)

[39] The Supreme Court of Canada stated in Ward v. Canada (Attorney General), [1993] 2 S.C.R. 689 at 747 that it is appropriate when considering claims to refugee status based on any of the grounds set out in the definition also to consider the perspective of the persecutor, because that is the perspective which is determinative in inciting the persecution. In discussing the risk to the applicant based on his appearance, the tribunal stated at page 7:
The panel asked the claimant whether his physical appearance would enable other Bulgarians to conclude he was Roma were he to appear on a street in Sofia. He said that other Bulgarians would know he was Roma because of his "bright picturesque clothing" but he later acknowledged that if he wore regular clothing it would be difficult to say he was Roma.
(emphasis added)

[40] And at page 8:
The panel concludes that the claimant would not be perceived to be Roma by fellow Bulgarians who possessed no specific knowledge of his alleged family antecedents. If he is indeed Roma, he is also very assimilated or, in his own words, "one of those Roma who are considered to be Bulgarian."
(emphasis added)

[41] And at page 17:
In the claimant's case, if he is indeed Roma through genetic inheritance, he has effectively transcended the Roma identity visibly, socially, and economically. Of course, someone somehow discovering his Roma ancestry might still seek to injure him. However, in a large center like Sofia it is safe to say that someone with the claimant's attributes and background would blend seamlessly into the Bulgarian majority. His risk of persecution is therefore effectively at the level of "mere possibility".
(emphasis added)

[42] The tribunal's analysis that the applicant is safe because other Bulgarians would not recognize him as being Roma is incomplete. In this instance, it was the authorities which were the source of the applicant's problems. That they have already determined that he is Roma belies the tribunal's assumption that his risk is a mere possibility. That they alr

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]

