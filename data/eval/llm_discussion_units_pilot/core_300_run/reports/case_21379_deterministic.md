# Discussion Units: case 21379

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **38**
- Continuity pairs: **37**
- Discussion Units: **2**
- Paragraph source hashes: **38**
- Sub-themes: **8**

## 21379:1 · paragraphs 0-35

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `2f82e41ad61772654ceb000f97d7f372bafa60f4d92585b6d7aabe178bf780ce`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 21379:1:subtheme:1 · paragraphs 0-3

- Raw key terms: `applicants, applicant, decision, fears, former, husband, immigration, police`
- Display key terms: `fears, former, husband, police`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule Display terms: fears, former, husband, police Rule/authority context: [1] This is an application pursuant to subsection 72(1) of the Immigration and Refugee Protection Act, S. Evidence spans paragraphs 0-3. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `determined that` at chunk `5004569` offsets `289-304`; context: 27 (the Act), for judicial review of a decision of the Refugee Protection Division of the Immigration and Refugee Board (the Board) dated August 3, 2007, wherein the Board determined that the applicants were not Convention refugees according to Section 96 of the Act, nor "persons in need of protection" according to Section 97 of the Act.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5004569` offsets `27-38`; context: [1] This is an application pursuant to subsection 72(1) of the Immigration and Refugee Protection Act, S.
- Evidence: `counterargument_limitation` cue `however` at chunk `5004571` offsets `347-354`; context: He complained to the police in October 2005, however they refused to register his complaint, and he was instructed to leave the perpetrator alone.

#### 21379:1:subtheme:2 · paragraphs 4-5

- Raw key terms: `claims, protection, adequate, applicant, applicants, applies, arrived, august`
- Display key terms: `claims, protection, adequate, applies, arrived, august`
- Argument roles: `evidence_fact, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, party_position, reasoning_application Display terms: claims, protection, adequate, applies, arrived, august Position/evidence statements: [4] The male applicant arrived in Canada on March 25, 2006 and claimed Refugee protection on March 28, 2006. Application context: The Board noted that as Mexico was a functioning democracy, the presumption of state protection applies, and thus, in order to rebut that presumption, the applicants must provide “clear and convincing” evidence that the  Evidence spans paragraphs 4-5. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `party_position` cue `claimed` at chunk `5004572` offsets `63-70`; context: [4] The male applicant arrived in Canada on March 25, 2006 and claimed Refugee protection on March 28, 2006.
- Evidence: `evidence_fact` cue `evidence` at chunk `5004573` offsets `372-380`; context: The Board noted that as Mexico was a functioning democracy, the presumption of state protection applies, and thus, in order to rebut that presumption, the applicants must provide “clear and convincing” evidence that the state is unable or unwilling to protect them.
- Evidence: `reasoning_application` cue `applies` at chunk `5004573` offsets `266-273`; context: The Board noted that as Mexico was a functioning democracy, the presumption of state protection applies, and thus, in order to rebut that presumption, the applicants must provide “clear and convincing” evidence that the state is unable or unwilling to protect them.

#### 21379:1:subtheme:3 · paragraphs 6-7

- Raw key terms: `applicant, board, claim, efforts, mexico, protection, provide, state`
- Display key terms: `efforts, mexico, protection, provide, state`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule Display terms: efforts, mexico, protection, provide, state Rule/authority context: The Board stated that local failures to provide protection do not amount to a lack of state protection and that pursuant to the documentary evidence, if the applicant was dissatisfied with police efforts or concerned tha Evidence spans paragraphs 6-7. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `counterargument_limitation` cue `However` at chunk `5004574` offsets `590-597`; context: However, while all of those efforts do not always provide protection to all citizens, the protection available was adequate.
- Evidence: `evidence_fact` cue `evidence` at chunk `5004575` offsets `295-303`; context: The Board stated that local failures to provide protection do not amount to a lack of state protection and that pursuant to the documentary evidence, if the applicant was dissatisfied with police efforts or concerned that police corruption was a factor, there were avenues open through which he could seek redress.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5004575` offsets `267-278`; context: The Board stated that local failures to provide protection do not amount to a lack of state protection and that pursuant to the documentary evidence, if the applicant was dissatisfied with police efforts or concerned that police corruption was a factor, there were avenues open through which he could seek redress.

#### 21379:1:subtheme:4 · paragraphs 8-9

- Raw key terms: `applicable, canada, court, determining, fact, legal, para, question`
- Display key terms: `applicable, determining, fact, legal, para, question`
- Argument roles: `governing_rule, issue`
- Explanation: Observed roles: governing_rule, issue Display terms: applicable, determining, fact, legal, para, question Rule/authority context: 11, I concluded that, given the nature of the question, as one of mixed fact and law, and the relative expertise of this Court in determining whether a legal standard has been met, the appropriate standard of review appl | New Brunswick, 2008 SCC 9, the question of the applicable standard of review must be revisited. Evidence spans paragraphs 8-9. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5004576` offsets `163-171`; context: 11, I concluded that, given the nature of the question, as one of mixed fact and law, and the relative expertise of this Court in determining whether a legal standard has been met, the appropriate standard of review applicable to determinations of state protection is one of reasonableness simpliciter.
- Evidence: `governing_rule` cue `standard of review` at chunk `5004576` offsets `314-332`; context: 11, I concluded that, given the nature of the question, as one of mixed fact and law, and the relative expertise of this Court in determining whether a legal standard has been met, the appropriate standard of review applicable to determinations of state protection is one of reasonableness simpliciter.
- Evidence: `issue` cue `question` at chunk `5004577` offsets `122-130`; context: New Brunswick, 2008 SCC 9, the question of the applicable standard of review must be revisited.
- Evidence: `governing_rule` cue `standard of review` at chunk `5004577` offsets `149-167`; context: New Brunswick, 2008 SCC 9, the question of the applicable standard of review must be revisited.

#### 21379:1:subtheme:5 · paragraphs 10-28

- Raw key terms: `protection, state, para, canada, citizenship, immigration, minister, mexico`
- Display key terms: `protection, state, para, mexico`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: protection, state, para, mexico Position/evidence statements: [12] The applicants argue that the Board erred in its state protection analysis and that a claim should not be rejected where there is evidence that state protection would either not be forthcoming or where it would be i | 54 the Federal Court of Appeal noted that “[t]he presumption of state protection described in Ward, therefore, applies equally to cases where an individual claims to fear persecution by non-state entities and to cases wh Rule/authority context: [10] In a recent decision, Madam Justice Eleanor Dawson, examined the standard of review applicable to findings regarding state protection and concluded that in light of Dunsmuir, above, the standard remains that of reas | [18] However, other jurisprudence has focussed on the problems that remain in Mexico’s democracy. Application context: 54 the Federal Court of Appeal noted that “[t]he presumption of state protection described in Ward, therefore, applies equally to cases where an individual claims to fear persecution by non-state entities and to cases wh | Therefore, the presumption of state protection is a strong one. Evidence spans paragraphs 10-28. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5004578` offsets `544-551`; context: Thus, pursuant to the reasonableness standard, the analysis of the Board’s decision will be concerned with “the existence of justification, transparency and intelligibility within the decision-making process [and also with] […] whether the decision falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and law” (Dunsmuir, above, at para.
- Evidence: `governing_rule` cue `standard of review` at chunk `5004578` offsets `70-88`; context: [10] In a recent decision, Madam Justice Eleanor Dawson, examined the standard of review applicable to findings regarding state protection and concluded that in light of Dunsmuir, above, the standard remains that of reasonableness (Eler v.
- Evidence: `issue` cue `issue` at chunk `5004579` offsets `23-28`; context: [11] The determinative issue in this application is the ability of the state of Mexico to adequately protect the applicants from their alleged persecutor, the principal applicant’s former husband, a police officer.
- Evidence: `party_position` cue `argue` at chunk `5004580` offsets `20-25`; context: [12] The applicants argue that the Board erred in its state protection analysis and that a claim should not be rejected where there is evidence that state protection would either not be forthcoming or where it would be ineffective.
- Evidence: `evidence_fact` cue `evidence` at chunk `5004580` offsets `135-143`; context: [12] The applicants argue that the Board erred in its state protection analysis and that a claim should not be rejected where there is evidence that state protection would either not be forthcoming or where it would be ineffective.
- Evidence: `party_position` cue `claims` at chunk `5004582` offsets `212-218`; context: 54 the Federal Court of Appeal noted that “[t]he presumption of state protection described in Ward, therefore, applies equally to cases where an individual claims to fear persecution by non-state entities and to cases where the state is alleged to be a persecutor.
- Evidence: `reasoning_application` cue `therefore` at chunk `5004582` offsets `156-165`; context: 54 the Federal Court of Appeal noted that “[t]he presumption of state protection described in Ward, therefore, applies equally to cases where an individual claims to fear persecution by non-state entities and to cases where the state is alleged to be a persecutor.
- Evidence: `counterargument_limitation` cue `notwithstanding` at chunk `5004584` offsets `465-480`; context: 18, I stated that:
[…] notwithstanding that not every member of the [police] was implicated in the applicant’s persecution, seeking help from the [police], - asking, in effect, the [police] to protect the applicant from itself – would have in all likelihood placed the applicant in greater peril.
- Evidence: `reasoning_application` cue `Therefore` at chunk `5004585` offsets `356-365`; context: Therefore, the presumption of state protection is a strong one.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `5004586` offsets `20-33`; context: [18] However, other jurisprudence has focussed on the problems that remain in Mexico’s democracy.
- Evidence: `evidence_fact` cue `evidence` at chunk `5004587` offsets `451-459`; context: 20-22, my colleague, Madam Justice Johanne Gauthier addressed the presumption of state protection in the context of Mexico’s democracy:
20 Mexico is a democracy to which a presumption of state protection applies, even if its place on the "democracy spectrum" needs to be assessed to determine what credible and reliable evidence will be sufficient to displace that presumption […]
21 In developed democracies such as the U.
- Evidence: `reasoning_application` cue `applies` at chunk `5004587` offsets `335-342`; context: 20-22, my colleague, Madam Justice Johanne Gauthier addressed the presumption of state protection in the context of Mexico’s democracy:
20 Mexico is a democracy to which a presumption of state protection applies, even if its place on the "democracy spectrum" needs to be assessed to determine what credible and reliable evidence will be sufficient to displace that presumption […]
21 In developed democracies such as the U.
- Evidence: `counterargument_limitation` cue `although` at chunk `5004587` offsets `1227-1235`; context: 22 The Court does not understand Hinzman to say that this conclusion applies to all countries wherever they stand on the "democracy spectrum" and to relieve the decision-maker of his or her obligation to assess the evidence offered to establish that, in Mexico for example, the state is unable (although willing) to protect its citizens, or that it was reasonable for the claimant to refuse to seek out this protection.
- Evidence: `evidence_fact` cue `evidence` at chunk `5004588` offsets `317-325`; context: Accordingly, decision-makers must engage in a full assessment of the evidence placed before them suggesting that Mexico, while willing to protect, may be unable to do so.
- Evidence: `reasoning_application` cue `I find` at chunk `5004588` offsets `5-11`; context: [20] I find Madam Justice Gauthier’s approach to the presumption of state protection in Mexico to be persuasive.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `5004589` offsets `178-191`; context: [21] I also note that with respect to avenues of protection that the applicants were required to exhaust, the applicants and the respondent have highlighted conflicting lines of jurisprudence.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `5004590` offsets `17-30`; context: [22] One line of jurisprudence holds that in seeking protection, an applicant is not required to “seek counselling, legal advice, or assistance from human rights agencies if the police are unable to help” (Malik v.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `5004591` offsets `21-34`; context: [23] Another line of jurisprudence holds that for the purposes of conducting a state protection analysis, state-run or state-funded agencies other than the police can be taken into account (Pal v.
- Evidence: `evidence_fact` cue `evidence` at chunk `5004593` offsets `120-128`; context: [25] I am of the view that these alternate institutions do not constitute avenues of protection per se; unless there is evidence to the contrary, the police force is the only institution mandated with the protection of a nation’s citizens and in possession of enforcement powers commensurate with this mandate.
- Evidence: `counterargument_limitation` cue `However` at chunk `5004594` offsets `114-121`; context: However, what was important was for the Board to be satisfied that the protection offered in Mexico was effective (Lopez v.
- Evidence: `evidence_fact` cue `evidence` at chunk `5004595` offsets `172-180`; context: [27] With respect to the principal applicant, who did not personally complain about the actions of her former husband, a police officer, the Board examined the documentary evidence and concluded that there were measures in place to deal with such a situation.
- Evidence: `counterargument_limitation` cue `However` at chunk `5004595` offsets `260-267`; context: However, the Board was faced with an abundance of evidence which indicated that these measures were not effective.
- Evidence: `evidence_fact` cue `evidence` at chunk `5004596` offsets `72-80`; context: [28] This Court has consistently held that where there is contradictory evidence before the Board, it must provide reasons why it did not consider this evidence relevant or trustworthy (Simpson v.

#### 21379:1:subtheme:6 · paragraphs 29-30

- Raw key terms: `abuse, against, board, domestic, finally, further, generally, indicates`
- Display key terms: `abuse, against, domestic, finally, further, generally, indicates`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: abuse, against, domestic, finally, further, generally, indicates Evidence spans paragraphs 29-30. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Issues` at chunk `5004597` offsets `109-115`; context: [29] More particularly, while the Board refers to the document entitled “Mexico: Domestic Violence and Other Issues Related to the Status of Women”, dated March 2003, it did not address portions of the same document which pointed to a different conclusion.

#### 21379:1:subtheme:7 · paragraphs 31-35

- Raw key terms: `board, protection, corruption, dated, entitled, further, human, light`
- Display key terms: `protection, corruption, dated, entitled, further, human, light`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, issue, party_position, reasoning_application Display terms: protection, corruption, dated, entitled, further, human, light Position/evidence statements: The Board was cognizant of the fact that the applicant complained directly to the police after his attack; however, it failed to mention the fact that he did submit a complaint to the Queretaro State Human Rights Commiss Application context: [35] Accordingly, the application for judicial review is allowed. Operative outcome context: [35] Accordingly, the application for judicial review is allowed. Evidence spans paragraphs 31-35. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5004599` offsets `9-14`; context: [31] The issue paper entitled “Mexico: Situation of Witnesses to Crime and Corruption, Women Victims of Violence and Victims of Discrimination Based on Sexual Orientation”, dated February 2007, again referred to by the Board, indicates in the “Effectiveness of protection efforts” section that the effectiveness of law enforcement and shelters in meeting the needs of victims could not be provided:
Regarding the effectiveness of protection available to women victims of violence interlocutors from both governmental and non-governmental organizations stated that evaluation efforts are relatively new and statistical information on, for example, the effectiveness of law enforcement and shelters in meeting the needs of victims could not be provided […]
- Evidence: `evidence_fact` cue `evidence` at chunk `5004600` offsets `941-949`; context: 63)
[Emphasis added]
The views of the Special Rapporteur present cogent evidence that despite the government of Mexico’s “due diligence”, the response to gender-based violence remains inadequate.
- Evidence: `party_position` cue `submit` at chunk `5004601` offsets `289-295`; context: The Board was cognizant of the fact that the applicant complained directly to the police after his attack; however, it failed to mention the fact that he did submit a complaint to the Queretaro State Human Rights Commission.
- Evidence: `counterargument_limitation` cue `however` at chunk `5004601` offsets `238-245`; context: The Board was cognizant of the fact that the applicant complained directly to the police after his attack; however, it failed to mention the fact that he did submit a complaint to the Queretaro State Human Rights Commission.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `5004603` offsets `5-16`; context: [35] Accordingly, the application for judicial review is allowed.
- Evidence: `disposition` cue `allowed` at chunk `5004603` offsets `57-64`; context: [35] Accordingly, the application for judicial review is allowed.

#### Section text

Flores Zepeda v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2008-04-16
Neutral citation
2008 FC 491
File numbers
IMM-3452-07
Notes
Reported Decision
Decision Content
Date: 20080416
Docket: IMM-3452-07
Citation: 2008 FC 491
Ottawa, Ontario, April 16, 2008
PRESENT: The Honourable Madam Justice Tremblay-Lamer
BETWEEN:
ROSARIO ADRIANA FLORES ZEPEDA,
GREGORIO MORENO QUINTANILLA, AND
VICTOR GUSTAVO RAMIREZ FLORES
Applicants
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
REASONS FOR JUDGMENT AND JUDGMENT

[1] This is an application pursuant to subsection 72(1) of the Immigration and Refugee Protection Act, S.C. 2001, c. 27 (the Act), for judicial review of a decision of the Refugee Protection Division of the Immigration and Refugee Board (the Board) dated August 3, 2007, wherein the Board determined that the applicants were not Convention refugees according to Section 96 of the Act, nor "persons in need of protection" according to Section 97 of the Act.

[2] The applicants are citizens of Mexico and residents of Queretaro State. The 32 year old female applicant, (the principal applicant) fears her former husband, from whom she was separated in 1997. She describes her former spouse as a violent, jealous and vengeful man who has often abused her and threatened to kidnap her son. She never approached the police for protection as her former husband was himself a policeman. She is also accompanied by her minor son.

[3] The male applicant is the common-law spouse of the principal applicant. He fears the principal applicant’s former husband, who threatened his life numerous times and beat him to the point of requiring hospitalization on one occasion in order to intimidate him into leaving the principal applicant. He complained to the police in October 2005, however they refused to register his complaint, and he was instructed to leave the perpetrator alone.

[4] The male applicant arrived in Canada on March 25, 2006 and claimed Refugee protection on March 28, 2006. The principal applicant and her son arrived in Canada on
June 10, 2006 and made their claims on the same day.

[5] In a decision dated August 3, 2007, the Board rejected the applicants’ claims for protection, as it was of the view that adequate state protection existed in Mexico. The Board noted that as Mexico was a functioning democracy, the presumption of state protection applies, and thus, in order to rebut that presumption, the applicants must provide “clear and convincing” evidence that the state is unable or unwilling to protect them.

[6] First, the Board analyzed the claim of the principal applicant. The Board noted that while there remain areas of protection for women which need to be improved, Mexico has taken great strides in protecting its female citizens in the Federal District (F.D.) of Mexico City. The Board was satisfied that a comprehensive legislative scheme was in place that gives victims of domestic violence both protection and recourse in the F.D., and that the state has put in place numerous initiatives that will assist a citizen in accessing the protection and recourse provided by the legislation. However, while all of those efforts do not always provide protection to all citizens, the protection available was adequate.

[7] Next, the Board examined the male applicant’s claim and focused on his failure to complain about the inefficiency of the police to other institutions. The Board stated that local failures to provide protection do not amount to a lack of state protection and that pursuant to the documentary evidence, if the applicant was dissatisfied with police efforts or concerned that police corruption was a factor, there were avenues open through which he could seek redress. The Board recognized that there is serious crime and corruption in Mexico, but documentary evidence indicates that serious efforts are being made by the government to tackle this problem as well as the problem with drug traffickers.
I. Standard of review

[8] In Chaves v. Canada (Minister of Citizenship and Immigration), 2005 FC 193, [2005] F.C.J. No. 232 (QL), at para. 11, I concluded that, given the nature of the question, as one of mixed fact and law, and the relative expertise of this Court in determining whether a legal standard has been met, the appropriate standard of review applicable to determinations of state protection is one of reasonableness simpliciter.

[9] However, in light of the recent decision of the Supreme Court of Canada in Dunsmuir v. New Brunswick, 2008 SCC 9, the question of the applicable standard of review must be revisited. The Supreme Court offered the following guidance in determining the standard of review:
[…] questions of fact, discretion and policy as well as questions where the legal issues cannot be easily separated from the factual issues generally attract a standard of reasonableness while many legal issues attract a standard of correctness. Some legal issues however, attract the more deferential standard of reasonableness. (at para. 51).
Further, at para. 62, the Court highlighted that the process of judicial review occurs in two stages:
First, courts ascertain whether the jurisprudence has already determined in a satisfactory manner the degree of defence to be accorded with regard to a particular category of question. Second, where the first inquiry proves unfruitful, courts must proceed to an analysis of the factors making it possible to identify the proper standard of review.

[10] In a recent decision, Madam Justice Eleanor Dawson, examined the standard of review applicable to findings regarding state protection and concluded that in light of Dunsmuir, above, the standard remains that of reasonableness (Eler v. Canada (Minister of Citizenship and Immigration), 2008 FC 334, at para. 6). Thus, pursuant to the reasonableness standard, the analysis of the Board’s decision will be concerned with “the existence of justification, transparency and intelligibility within the decision-making process [and also with] […] whether the decision falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and law” (Dunsmuir, above, at para. 47).
II. Analysis

[11] The determinative issue in this application is the ability of the state of Mexico to adequately protect the applicants from their alleged persecutor, the principal applicant’s former husband, a police officer.

[12] The applicants argue that the Board erred in its state protection analysis and that a claim should not be rejected where there is evidence that state protection would either not be forthcoming or where it would be ineffective. The respondent submits that given the fact that Mexico is a democracy, the presumption of state protection is a strong one and the applicants have not provided clear and cogent evidence capable of rebutting it.

[13] It is true that “clear and convincing confirmation” of a state’s inability to protect must be put forth by an applicant, and that absent such proof, it is to be presumed that a state can protect its own citizens (Canada (Attorney General) v. Ward, [1993] 2 S.C.R. 689, at pages 724-725, [1993] S.C.J. No. 74 (QL), at para. 50). In this context, the more democratic a state is, the more the individual must have done to exhaust all avenues of protection available (Kadenko v. Canada (Solicitor General) (1996), 143 D.L.R. (4th) 532, at p. 534, [1996] F.C.J. No. 1376 (QL), at para. 5; Hinzman v. Canada (Minister of Citizenship and Immigration), 2007 FCA 171, [2007] F.C.J. No. 584 (QL), at para. 57).

[14] In the recent decision of Hinzman, above, at para. 54 the Federal Court of Appeal noted that “[t]he presumption of state protection described in Ward, therefore, applies equally to cases where an individual claims to fear persecution by non-state entities and to cases where the state is alleged to be a persecutor.” Thus, the existence of state persecuting agents does not serve to automatically rebut the presumption that a state is capable of protecting its citizens.

[15] The Court of Appeal expounded upon the nature of the burden imposed upon claimants when attempting to rebut the presumption of state protection:
Kadenko and Satiacum together teach that in the case of a developed democracy, the claimant is faced with the burden of proving that he exhausted all the possible protections available to him and will be exempted from his obligation to seek state protection only in the event of exceptional circumstances: Kadenko at page 534, Satiacum at page 176. (Hinzman, above, at para. 57)

[16] While the burden placed on claimants from developed democratic states is a high one, I remain of the view that this burden does not require that they put themselves in danger in order to exhaust all possible avenues of protection. Indeed, as Justice LaForest indicated, an individual will be required to seek state protection where it would be objectively unreasonable not to do so (Ward, above, at para. 49). In Chaves, above, at para. 18, I stated that:
[…] notwithstanding that not every member of the [police] was implicated in the applicant’s persecution, seeking help from the [police], - asking, in effect, the [police] to protect the applicant from itself – would have in all likelihood placed the applicant in greater peril.
Indeed, in my opinion, the requirement of having to place oneself in danger in order to exhaust all protection avenues would constitute an “exceptional circumstance” referred to by the Federal Court of Appeal above.

[17] With respect to the strength of the applicable presumption in Mexico, the respondent cites the case of Velazquez v. Canada (Minister of Citizenship and Immigration), 2006 FC 532, [2006] F.C.J. No. 663 (QL), at para. 6, in which Justice Michael Phelan stated “Mexico is a functioning democracy, and a member of the NAFTA, with democratic institutions. Therefore, the presumption of state protection is a strong one.” (see also Canseco v. Canada (Minister of Citizenship and Immigration), 2007 FC 73, [2007] F.C.J. No. 115 (QL), at para. 14; Alfaro v. Canada (Minister of Citizenship and Immigration), 2006 FC 460, [2006] F.C.J. No. 569 (QL), at para. 18, highlighting the free and democratic nature of Mexican society).

[18] However, other jurisprudence has focussed on the problems that remain in Mexico’s democracy. Recently, Deputy Justice Orville Frenette in De Leon v. Canada (Minister of Citizenship and Immigration), 2007 FC 1307, [2007] F.C.J. No. 1684 (QL), at para. 28 indicated that as a developing democracy with problems including corruption and drug trafficking involving state authorities, the presumption of state protection applicable to Mexico is more easily overturned.

[19] Similarly in Capitaine v. Canada (Minister of Citizenship and Immigration), 2008 FC 98, [2008] F.C.J. No. 181 (QL), at paras. 20-22, my colleague, Madam Justice Johanne Gauthier addressed the presumption of state protection in the context of Mexico’s democracy:
20 Mexico is a democracy to which a presumption of state protection applies, even if its place on the "democracy spectrum" needs to be assessed to determine what credible and reliable evidence will be sufficient to displace that presumption […]
21 In developed democracies such as the U.S. and Israel, it is clear from Hinzman (at paras. 46 and 57) that to rebut the presumption of state protection, this evidence must include proof that an applicant has exhausted all recourses available to her or him. It is also clear that, except in exceptional circumstances, it would be unreasonable in such countries not to seek state protection before seeking it in Canada.
22 The Court does not understand Hinzman to say that this conclusion applies to all countries wherever they stand on the "democracy spectrum" and to relieve the decision-maker of his or her obligation to assess the evidence offered to establish that, in Mexico for example, the state is unable (although willing) to protect its citizens, or that it was reasonable for the claimant to refuse to seek out this protection. […]

[20] I find Madam Justice Gauthier’s approach to the presumption of state protection in Mexico to be persuasive. While Mexico is a democracy and generally willing to protect its citizens, its governance and corruption problems are well documented. Accordingly, decision-makers must engage in a full assessment of the evidence placed before them suggesting that Mexico, while willing to protect, may be unable to do so. This assessment should include the context of the country of origin in general, all the steps that the applicants did in fact take, and their interaction with the authorities (Hernandez v. Canada (Minister of Citizenship and Immigration), 2007 FC 1211, [2007] F.C.J. No. 1563 (QL), at para. 21; G.D.C.P. v. Canada (Minister of Citizenship and Immigration), 2002 FCT 989, [2002] F.C.J. No. 1331 (QL), at para. 18).

[21] I also note that with respect to avenues of protection that the applicants were required to exhaust, the applicants and the respondent have highlighted conflicting lines of jurisprudence.

[22] One line of jurisprudence holds that in seeking protection, an applicant is not required to “seek counselling, legal advice, or assistance from human rights agencies if the police are unable to help” (Malik v. Canada (Minister of Citizenship and Immigration), 2003 FCT 453, [2003] F.C.J. No. 645 (QL), at para. 21; Molnar v. Canada (Minister of Citizenship and Immigration), [2003] F.C. 339, [2002] F.C.J. 1425 (QL), at paras. 23-24).

[23] Another line of jurisprudence holds that for the purposes of conducting a state protection analysis, state-run or state-funded agencies other than the police can be taken into account (Pal v. Canada (Minister of Citizenship and Immigration), 2003 FCT 698, [2003] F.C.J. No. 894 (QL), at para. 5; Nagy v. Canada (Minister of Citizenship and Immigration), 2002 FCT 281, [2002] F.C.J. No. 370 (QL); Szucs v. Canada (Minister of Citizenship and Immigration), [2000] F.C.J. No. 1614 (QL), at para. 29).

[24] In the present case, the Board proposed a number of alternate institutions in response to the applicants’ claim that they were dissatisfied with police efforts and concerned with police corruption, including National or State Human Rights Commissions, the Secretariat of Public Administration, the Program Against Impunity, the General Comptroller’s Assistance Directorate or through a complaints procedure at the Office of the Attorney General (PGR).

[25] I am of the view that these alternate institutions do not constitute avenues of protection per se; unless there is evidence to the contrary, the police force is the only institution mandated with the protection of a nation’s citizens and in possession of enforcement powers commensurate with this mandate. For example, the documentary evidence explicitly states that the National Human Rights Commission has no legal power of enforcement (“Mexico: Situation of Witness to Crime and Corruption, Women Victims of Violence and Victims of Discrimination Based on Sexual Orientation”).

[26] The Board’s decision points to many efforts being made by the state to protect women from domestic violence. However, what was important was for the Board to be satisfied that the protection offered in Mexico was effective (Lopez v. Canada (Minister of Citizenship and Immigration), 2007 FC 1341, [2007] F.C.J. No. 1733 (QL), at para. 16; Garcia v. Canada (Minister of Citizenship and Immigration), 2007 FC 79, [2007] F.C.J. No. 118 (QL), at para. 15; Avila v. Canada (Minister of Citizenship and Immigration), 2006 FC 359, [2006] F.C.J. No. 439 (QL), at para. 34; Elcock v. Canada (Minister of Citizenship and Immigration), [1999] F.C.J. No. 1438 (QL), at para. 15).

[27] With respect to the principal applicant, who did not personally complain about the actions of her former husband, a police officer, the Board examined the documentary evidence and concluded that there were measures in place to deal with such a situation. However, the Board was faced with an abundance of evidence which indicated that these measures were not effective.

[28] This Court has consistently held that where there is contradictory evidence before the Board, it must provide reasons why it did not consider this evidence relevant or trustworthy (Simpson v. Canada (Minister of Citizenship and Immigration), [2006] FC 970, [2006] F.C.J. No. 1224 (QL), at para. 44; Castillo v. Canada (Minister of Citizenship and Immigration), 2004 FC 56, [2004] F.C.J. No. 43 (QL), at para. 9; Cepeda-Gutierrez v. Canada (Minister of Citizenship and Immigration), [1998] F.C.J. No. 1425 (QL), at para. 15).

[29] More particularly, while the Board refers to the document entitled “Mexico: Domestic Violence and Other Issues Related to the Status of Women”, dated March 2003, it did not address portions of the same document which pointed to a different conclusion. For example, excerpts indicated that domestic abuse occurs in one of every three homes in Mexico. Further, according to the Justice Attorney General’s Office of the Federal District, 48% of homicides committed in 2001 were attributed to domestic violence. The document also indicated that Mexican society generally considers domestic violence to be a private matter and police are reluctant to intervene. With respect to the availability of shelters for women who are victims of violence, the document indicates that according to COVAC [Mexican Association Against Violence Towards Women] “existing shelters established for victims of violence are saturated and that the assistance that can be received is temporary and does not generally respond to the growing need in the cities.” Finally, according to Marta Torres, Coordinator of the Interdisciplinary Women’s Studies Program at the Colegio de México, “despite the progress made in the legislative field, the existing legislation on spousal abuse has not yet had a decisive impact.”

[30] The 2006 U.S. State Department Report on Mexico, also specifically referred to by the Board, indicates that at the state level, laws sanctioning domestic violence, if any, are weak, and victims generally do not report abuse for many reasons, including disinterest of authorities in prosecuting such offences. Further, violence against women remained a widespread phenomenon throughout the country; on an annual basis approximately 1,600 women were killed nationwide mostly from domestic violence. Finally, in August the UN Committee for the Elimination of Discrimination Against Women said that there were no visible results from government efforts to prevent gender violence.

[31] The issue paper entitled “Mexico: Situation of Witnesses to Crime and Corruption, Women Victims of Violence and Victims of Discrimination Based on Sexual Orientation”, dated February 2007, again referred to by the Board, indicates in the “Effectiveness of protection efforts” section that the effectiveness of law enforcement and shelters in meeting the needs of victims could not be provided:
Regarding the effectiveness of protection available to women victims of violence interlocutors from both governmental and non-governmental organizations stated that evaluation efforts are relatively new and statistical information on, for example, the effectiveness of law enforcement and shelters in meeting the needs of victims could not be provided […]

[32] Further, in the National Documentation Package provided to the Board was a document entitled “Integration of the Human Rights of Women and a Gender Perspective: Violence Against Women”, dated January 13, 2006 (National Documentation Package on Mexico, item 5.15). This report by the United Nations Special Rapporteur on violence against women regarding the situation in Mexico, instructively states the following:
The Government of Mexico has taken significant steps to prevent, punish and eradicate violence against women with due dilige

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]


## 21379:2 · paragraphs 36-37

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `249895ba664d6427bcd4a99c2bcd7c853369504684e0504be429fc91093ef781`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 21379:2:subtheme:1 · paragraphs 36-37

- Raw key terms: `judgment, tremblay-lamer, adriana, allowed, anani, appearances, applicant, application`
- Display key terms: `tremblay-lamer, adriana, allowed, anani`
- Argument roles: `disposition`
- Explanation: Observed roles: disposition Display terms: tremblay-lamer, adriana, allowed, anani Operative outcome context: JUDGMENT THIS COURT ORDERS that the application for judicial review is allowed. Evidence spans paragraphs 36-37. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `disposition` cue `allowed` at chunk `5004603` offsets `226-233`; context: JUDGMENT
THIS COURT ORDERS that the application for judicial review is allowed.

#### Section text

JUDGMENT
THIS COURT ORDERS that the application for judicial review is allowed. The matter is returned to a newly constituted Board for re-hearing and re-determination.
“Danièle Tremblay-Lamer”
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET: IMM-3452-07
STYLE OF CAUSE: ROSARIO ADRIANA FLORES ZEPEDA,
GREGORIO MORENO QUINTANILLA, AND
VICTOR GUSTAVO RAMIREZ FLORES
v.
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
PLACE OF HEARING: Toronto, Ontario
DATE OF HEARING: April 9, 2008
REASONS FOR JUDGMENT
AND JUDGMENT: TREMBLAY-LAMER J.
DATED: April 16, 2008
APPEARANCES:
Lina Anani
FOR THE APPLICANT
Asha Gafar
FOR THE RESPONDENT
SOLICITORS OF RECORD:
Lina Anani
Barrister and Solicitor
181 Eglinton Avenue East,
Suite 206
Toronto (ON) M4P 1J4
FOR THE APPLICANT
John H. Sims
Department of Justice Canada
130 King Street West, Suite 3400
Toronto, Ontario M5X 1K6
FOR THE RESPONDENT
