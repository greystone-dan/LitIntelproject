"""Words for the Coming soon pages.

Each item: (anchor, title, status, [paragraphs], example, today, needs).
Statuses are honest: built, partly, progress, planned, concept. Nothing here needs AI
when someone uses the site; where AI appears it is optional, on the agency's own
computers, and its output is stored as data that points back to the source text.
"""

from __future__ import annotations

SECTIONS = {
	"accuracy": {
		"label": "Accuracy improvements",
		"summary": "Making what is already in the library more correct.",
		"lede": "Every screen in iLit sits on top of the same raw material: citations, links, labels, names and outcomes worked out from the text of decisions. If a link goes to the wrong case or an outcome is coded the wrong way, every feature built on it inherits the mistake. This area is the work of getting those foundations right before the library grows.",
		"why": "For litigation counsel the cost of an error is not an inconvenience, it is a risk: a wrongly resolved citation can send someone to the wrong authority, and a wrong outcome can distort a statistic quoted to a manager. That is why the work here is slow, checked against hand-graded samples, and switched on only once it measures well.",
		"items": [
			("citation-extraction", "Citation extraction", "partly", [
				"Finding every citation inside a decision, including the awkward ones: short forms such as “Baker, at para 44”, citations that carry a pinpoint, parallel citations to the same case, and statutes cited by section.",
				"A second set of rules has been written and tested. It has been run into separate tables for a first batch of decisions, so it can be compared with the current results without touching what the site shows.",
			], "Reading a Federal Court decision, you click the citation of a leading case and land on the paragraph the judge was actually pointing to, not just the top of the case.",
			"The refined rules exist and have run over a first batch of several thousand decisions. The live site still reads the earlier citation records.",
			"A full run over the library, a before-and-after comparison on real cases, and a decision to switch the site over (keeping the old records as a fallback)."),
			("citation-resolving", "Citation resolving and pinpoints", "partly", [
				"Resolving means deciding which case a citation refers to. Most links are right today, but some short-form references point to the wrong case, and a few citations that should carry a paragraph number lose it.",
				"Recent rule changes keep pinpoints after parallel citations, narrative clauses and name-plus-year references. Rebuilding the links with those rules is the next step.",
			], "A memo cites “Vavilov at para 85”. The reader opens the right case at that paragraph, and says plainly when it could not tell which case was meant.",
			"The new rules are merged and tested. The library has not yet been rebuilt with them.",
			"A rebuild of the links, then a spot check on a graded sample before anything is shown as resolved."),
			("case-types", "Case types", "partly", [
				"A case type says what kind of proceeding a decision is, for example a leave application, a judicial review of a refugee decision or a stay motion. It makes searches and statistics far more useful, because a filter by outcome means little if different kinds of case are mixed together.",
				"Case types are assigned by fixed rules, not by an AI model, so the same decision always gets the same label and the reason can be shown.",
			], "Filtering to judicial reviews of Refugee Protection Division decisions decided in the last five years, without stay motions and leave decisions diluting the numbers.",
			"Live for the Federal Court, the Refugee Protection Division and the Supreme Court. Federal Court of Appeal types are held back because their accuracy is below the bar.",
			"Better rules for the Federal Court of Appeal, checked against a hand-graded sample, then the same for the Refugee Appeal Division."),
			("outcome-coding", "Outcome coding", "progress", [
				"Outcome coding records who won: the Minister or the applicant. It is the number behind judge profiles, issue statistics and any statement about how often a point succeeds, so it has to be close to right.",
				"It is being re-checked against a hand-reviewed set of 587 cases. Some well-known decisions are known to be coded the wrong way on the live site until the re-run is done, and the site shows those figures with their counts for that reason.",
			], "Before quoting a success rate in a briefing note, you can see how many decisions sit behind it and how many could not be classified.",
			"Outcome coding runs and a reviewed set exists. A re-run with corrected rules is waiting to be applied.",
			"Applying the re-run, a before-and-after report, and an agreed accuracy target before any rate is presented as reliable."),
			("statute-references", "Statute references", "progress", [
				"Decisions cite sections of the Immigration and Refugee Protection Act, its regulations and other statutes in many different forms. Reading those references correctly lets the site answer “which decisions apply section 34(1)(f)?” and link each reference to the text of the provision.",
				"A fresh read of the statutes cited is being done in stages. The first batch is being graded by hand, and the remaining cases wait on that result.",
			], "Starting from section 34(1)(f), you see every decision in the library that applies it, by year, court and outcome.",
			"Statute references exist for the whole library from the earlier reading. A more careful re-read has run over a first batch of cases.",
			"Finishing the grading of the first batch, a decision on the rest, and a clear label on each reference showing how it was read."),
			("judges", "Judges and decision-makers", "partly", [
				"Judge names appear in many forms in the sources, so one judge can show up as several profiles. Some names have also been merged that should not have been, such as two judges who share a surname but sit on different courts.",
				"Merged names are being corrected, and the gaps are being filled: some Federal Court decisions have no judge recorded, and the Refugee Protection Division’s decision-makers are blank.",
			], "Opening a judge profile and trusting that it holds that judge’s decisions and only theirs.",
			"Judge Profiles are live. Many spelling variants are merged. A few wrong merges and several extraction gaps remain.",
			"Pruning the wrong merges, extracting names where they are missing, and covering French-language decisions."),
			("show-your-work", "Showing how each label was assigned", "planned", [
				"Next to a case type, an outcome, a tag or a link, the site would show in plain words how it was decided: which rule fired and which words in the decision triggered it.",
				"This matters because a label you cannot check is a label you cannot rely on in front of a tribunal or a supervisor.",
			], "Clicking an outcome label and seeing the sentence in the decision that produced it.",
			"Some labels already link back to their source text. There is no common “how assigned” line.",
			"Recording the reason at the time each label is made, and a small design for showing it without clutter."),
		],
	},
	"expansion": {
		"label": "Expansion",
		"summary": "More cases, more tags, more laws and regulations.",
		"lede": "A library is only useful for the questions it can answer. Today iLit holds decisions of the Federal Court, the Federal Court of Appeal, the Supreme Court of Canada and the Refugee Protection Division, with the Refugee Appeal Division being added. This area is about widening that coverage and keeping it current, without lowering the quality bar set by the accuracy work.",
		"why": "Counsel working a file rarely stops at one court. A judicial review of a refugee decision depends on the tribunal’s own decisions, the Court’s case law and the statutes behind both. The more of that sits in one searchable place, the less time is spent hunting across websites.",
		"items": [
			("more-cases", "More cases", "progress", [
				"Refugee Appeal Division decisions are being loaded, and the earlier years of the Refugee Protection Division are being added from an open research dataset. Each decision keeps a link to its original source.",
				"New decisions go through the same reader, citation and statute tools as the rest of the library, so a larger library does not mean a different experience.",
			], "Checking how the Refugee Appeal Division has treated a credibility finding, then following a Federal Court review of the same decision.",
			"Federal Court, Federal Court of Appeal, Supreme Court and Refugee Protection Division are in. Refugee Appeal Division loading is under way.",
			"Finishing the loads, checking case types and names on the new decisions, and recording where each batch came from."),
			("daily-intake", "Keeping the library current", "partly", [
				"New Federal Court decisions are published every day. A daily intake job finds them, downloads them and adds them to the library, running the same checks as the original load.",
				"The job is built and has been run by hand. It is not yet on a schedule, because scheduling it needs sign-off on the computer that runs the site.",
			], "A decision released this morning being searchable by the afternoon, without anyone running a script.",
			"Built and tested, but run by hand and not scheduled.",
			"Sign-off to schedule it, a quiet failure alert so a missed day is noticed, and a short log of what each run added."),
			("more-tags", "More tags", "planned", [
				"Tags describe what a decision is about: the legal issues, the grounds raised, the statute sections applied. They drive filters, statistics and “find similar” features.",
				"The current tag set works, and the rules that produce it are fixed and inspectable. A wider set would let searches go deeper, for example by naming the specific ground of inadmissibility or the type of procedural fairness complaint.",
			], "Finding every decision on a particular ground of inadmissibility and comparing outcomes by year.",
			"A working tag set exists, with filters and statistics built on it.",
			"Agreement on the list of new tags, rules for each, and a check against hand-graded decisions before any is shown."),
			("laws-regulations", "More laws and regulations", "partly", [
				"Decisions rely on statutes, regulations and sometimes ministerial instructions. The library holds the main federal immigration instruments so that a section cited in a decision can be read in place.",
				"Quebec, Civil Code and other provincial material is left out for now, by decision. The aim is to be complete for federal immigration work first.",
			], "Opening a cited regulation section from the reader and seeing the wording, plus every decision that cites it.",
			"A federal statute library exists. Provincial statutes are deliberately excluded for now.",
			"A list of the remaining federal instruments and policy materials in scope, and a way to show which version was in force when a decision was made."),
			("french", "French-language counterparts", "planned", [
				"A few hundred French-language decisions are in the library, mostly Federal Court. Each decision is stored in one language, so an English decision’s French counterpart is not linked to it.",
				"Counsel working in French, or comparing the two versions of a decision, would need both stored and joined.",
			], "Opening a decision and switching to its French version at the same paragraph.",
			"Some French decisions are stored. None from the Refugee Appeal Division or Refugee Protection Division. No counterpart linking.",
			"Scoping which decisions have French counterparts, storing both languages, and linking paragraph to paragraph."),
			("id-iad", "Immigration Division and Immigration Appeal Division", "concept", [
				"Decisions of the Immigration Division and the Immigration Appeal Division are not published in the datasets used so far, so the library holds none of them. For hearings work this is the largest gap.",
				"Closing it depends on a lawful source and terms of use, not on technology. Where the agency holds the decisions itself, they would belong with the internal documentation described under that area.",
			], "Reading an admissibility decision next to the Federal Court judicial review of it.",
			"None are held.",
			"A confirmed source, terms of use and privacy approval, then the same import and tagging as other decisions."),
		],
	},
	"internal": {
		"label": "Internal documentation",
		"summary": "The agency’s own materials, searched beside the public library.",
		"lede": "The public library is the starting point. The larger value for a litigation division is its own material: hearing briefs, legal opinions, memos, notes on what has persuaded members, and private decisions. This area describes how that material could be searched and analysed beside the public library, on the agency’s own computers, with the same reader, citations and statute links and with nothing leaving the building.",
		"why": "A litigator’s best precedent is often something the division wrote last year, not something a court published. Today that knowledge lives in folders and in people’s memories. Making it searchable the way public decisions are, and labelled so nobody mistakes an internal note for a public authority, is the single biggest change iLit could make for the Division.",
		"note": "Everything in this area is concept except where an item says otherwise. Nothing internal is held by the live site, and the live site has no agency sign-in. These items describe an on-premises version that would be built with the agency’s information-security and privacy teams.",
		"items": [
			("internal-documents", "Internal documents, searchable", "concept", [
				"Hearing briefs, opinions and memos would be read, tagged and indexed by the same fixed rules as public decisions, so a search for a legal test returns the public cases and the agency’s own papers together.",
				"Every result is labelled internal or public, and a click opens the same formatted reader with the citations and statutes linked.",
			], "Searching “organization, section 34(1)(f)” and seeing a 2022 Legal Services memo and the Federal Court decisions it relied on in one list.",
			"Nothing internal is held. The reader, citation extraction and statute linking already work on any decision text.",
			"A list of the document types in scope and how they are brought in, an on-premises install, agency sign-in and approval from security and privacy."),
			("agency-repositories", "Agency repositories and private ID and IAD decisions", "concept", [
				"The agency holds decisions and files the public cannot see, such as Immigration Division and Immigration Appeal Division decisions. An agency copy of iLit could search them together with the public library, with a clear switch for each source.",
				"This also fills the biggest gap in the public library, since those tribunals’ decisions are not in any public dataset.",
			], "Turning on the agency repository as well as the public library, then finding how members have ruled on a ground and which Federal Court decisions reviewed them.",
			"Only public decisions are held. There is no agency sign-in and no private record on the live site.",
			"Agreed connections to each repository, handling rules, a security review and approval to copy or index each source."),
			("handling-marks", "Source and handling marks", "concept", [
				"Every result would show where it came from and how it must be handled: public, internal, protected. The mark would travel with the text into excerpts, exports and printouts.",
				"The aim is that nobody can copy an internal paragraph into a public document without being told what it is.",
			], "Exporting a research note and seeing each excerpt tagged with its source and handling level.",
			"Public decisions link to their original source. There are no handling levels.",
			"The agency’s handling categories, a place to store the mark with each document and rules for exports."),
			("argument-identification", "Argument identification on your own file", "partly", [
				"Open a memorandum, list each argument it makes, show which the other side has answered, and point to the authorities that bear on each. A person decides what to file; the tool only organises the file.",
				"Live Analysis in the Workbench already lists the cases and statutes a memo cites, with paragraph links. Identifying the arguments themselves is not built.",
			], "Dropping in an applicant’s memorandum and seeing a table of arguments, with a flag where the respondent has not yet replied.",
			"Live Analysis reads an uploaded file in memory, lists its cases and statutes and keeps nothing.",
			"A way to identify arguments without sending text outside the agency, and lawyer review of the suggestions on real memoranda."),
			("memo-check", "Memo citation check and gap check", "partly", [
				"A citation check lists the authorities a memo cites, shows how each has since been treated, and flags those that look overturned or questioned. A gap check suggests commonly cited authorities on related issues that the memo does not mention.",
				"Early versions exist. The gap check works on decisions already in the library, not on uploaded briefs.",
			], "Running a draft factum through the check the day before filing and finding a case that was overturned last year.",
			"Early versions open from the Development tab.",
			"Reliable treatment labels (see Increased intelligence) and a version that works on uploaded documents without storing them."),
			("institutional-memory", "The Division’s earlier positions", "concept", [
				"Past submissions and notes on what has persuaded members could be searched by issue, so a new file starts from what the Division has already argued, not from a blank page.",
				"Each position would link to the authorities it relied on and show how those have fared since.",
			], "Starting a new file on a ground of inadmissibility and seeing the arguments the Division used in the last five similar files.",
			"Nothing is held.",
			"Internal documents in the library, agreed rules on what may be indexed, and a way to keep client and privilege markings intact."),
			("deidentify", "De-identify before sharing", "partly", [
				"A decision or memo often has to be shared outside the file team, for training or for a research question. A de-identify tool replaces names and identifiers with placeholders and gives the person a key to reverse it.",
				"The tool exists in the Workbench. It hands the key to the person using it and does not keep it.",
			], "Preparing an example for a training session with every name replaced and the key kept on your own computer.",
			"Available in the Workbench as an early version.",
			"More identifier types, a review step before release and agency approval of its rules."),
		],
	},
	"intelligence": {
		"label": "Increased intelligence",
		"summary": "Features that read the decisions, not just list them.",
		"lede": "Finding a case is only the first step. Counsel need to know how an authority has been treated since, which argument a paragraph is making, which cases sit near each other and how a decision-maker has ruled on an issue. This area is about features that answer those questions by reading the structure of decisions.",
		"why": "The goal is less time reading and more time deciding. A tool that shows that an authority was followed in most later cases, and which later decisions departed from it, replaces an afternoon of citation checking. Every claim has to be traceable to a paragraph, because counsel have to stand behind what they cite.",
		"note": "Where AI would help, such as writing a one-line summary of how a case was used, it would run on an on-premises model when decisions are added, and the result would be stored as data with a link to the source paragraph. The live site makes no AI call when someone searches.",
		"items": [
			("citation-treatment", "Citation treatment", "concept", [
				"Treatment says how a later decision used an earlier authority: followed, applied, distinguished, questioned or criticised. Shown beside each citing paragraph, with a warning when the tide turns, it replaces manual citation checking.",
				"Treatment labels have been tried offline on a small labelled sample. Nothing is shown on the site.",
			], "Opening a leading case and seeing that it was followed in most later decisions but distinguished in the last three, each linked to its paragraph.",
			"Citation Intelligence is live: who cites a case, how that changed over time and the outcomes of the citing decisions. Treatment labels exist only as an offline trial.",
			"Labels assigned per citing paragraph with a visible “how assigned” line, review of a sample by lawyers, and refined citation links underneath."),
			("citation-enhancements", "AI-backed citation enhancements", "concept", [
				"On top of the rule-based links, an on-premises model could write a plain-language line saying why a case was cited, or flag a citation whose treatment is unclear.",
				"The line would be written once, when the decision is added, and stored with a link to the paragraph it summarises. Nobody’s search would be sent to a model.",
			], "Reading a list of citing paragraphs with a one-line reason for each, and clicking through to confirm it.",
			"Not built. There is no model installed.",
			"The on-premises model (see Local private AI), reviewed examples to test it against, and a rule that anything unreviewed is labelled as such."),
			("discussion-units", "Discussion units and argument subsections", "partly", [
				"A decision is long, but it has a shape: the facts, the legal test, the analysis, the disposition. Discussion units mark those parts and the argument subsections inside them, so a search can land on the part that states the test.",
				"A rule-based version has been built and tested in a sandbox. It is not yet stored in the database.",
			], "Searching “test for reasonable apprehension of bias” and landing on the paragraphs that state the test, not on a passage that merely mentions it.",
			"The outline of headings is live in the reader. Discussion units run in a testing page and as reports.",
			"Review of the unit boundaries against a hand-checked set, then storing units when decisions are added and search by unit."),
			("themes", "Themes", "partly", [
				"Themes group the arguments that recur across decisions, such as the recurring complaints about credibility findings or about reasons for a refusal, and show which statutory provisions each one leans on.",
				"A first Legal Themes page exists. It is built on tags and will be sharper once discussion units are stored.",
			], "Seeing the three most common ways applicants attack a credibility finding, with a sample decision for each.",
			"A Legal Themes and Statutes page opens from the Development tab.",
			"Stored discussion units, better tags and a plain-language label for each theme."),
			("neighbourhoods", "Citation neighbourhoods", "partly", [
				"Start from one case and see what it relies on, what cites it and what is cited alongside it, grouped by issue. Compare two cases and see the authorities they share.",
				"The Citation Map page does the first part today. Grouping by issue and showing neighbourhoods inside the reader come next.",
			], "Starting from a leading decision and finding the other authorities that are always cited with it.",
			"Citation Map opens from the Development tab.",
			"Cleaner citation links, grouping by issue and a neighbourhood panel in the reader."),
			("fingerprints", "Case fingerprints and similar cases", "partly", [
				"A fingerprint describes a decision by its tags, statute sections and cited authorities. Two decisions with similar fingerprints are similar cases, and the site can say why.",
				"The method is built without AI and tested on several thousand decisions. The reader has a Similar cases panel that reads stored fingerprints.",
			], "Opening a decision and getting a list of similar cases, each with the reason: same ground, same sections, six authorities in common.",
			"The method is tested and the panel exists. Fingerprints have not been computed for the whole library.",
			"Computing them for every decision, a plain-words reason for each match and spot checks by a lawyer."),
			("decision-maker-insights", "Judge and decision-maker insights", "partly", [
				"How a judge or Board member has ruled on a particular issue, with the count beside every figure and a warning when the number is small. These are descriptions of past decisions, not predictions.",
				"Judge Profiles are live. The numbers are only as good as the outcome coding and the judge names beneath them, which is why the accuracy work comes first.",
			], "Checking how often a judge has ruled for the Minister on procedural fairness, and seeing that the figure rests on twelve decisions.",
			"Judge Profiles are live with counts and unclassified decisions shown.",
			"Finished name cleanup, extraction where names are missing and outcome accuracy close to complete before any rate is quoted."),
		],
	},
	"team": {
		"label": "Team features",
		"summary": "Working on cases together.",
		"lede": "Today the site is a single shared view. Nobody has an account, and nothing a person saves belongs to them. A litigation division works in teams on files that last months, so the useful next step is to let people keep their own work, share it with a colleague and hand it off.",
		"why": "A research tool that cannot remember what you found yesterday, or show a colleague what you checked, forces the work to move to Word and email. Accounts, shared folders and notes keep it with the sources, and give a supervisor a way to see what was checked and when.",
		"note": "None of these need AI. They need real sign-in, which is why they depend on a deployment inside the agency, with its own accounts, rather than on the public site.",
		"items": [
			("accounts", "Accounts and roles", "planned", [
				"Each person signs in as themselves, and what they save belongs to them. Roles decide who can see what: an analyst, a counsel, a team lead.",
				"On an agency network the sign-in would use the agency’s own accounts, so nobody has to create a new password.",
			], "Signing in and finding your saved searches and pinned cases exactly as you left them.",
			"No sign-in. The Workbench has a demo mode where a typed name picks a private bucket, with no password or account.",
			"A deployment where real sign-in makes sense and a decision on roles."),
			("teams", "Teams and shared folders", "planned", [
				"A team folder for a file or a topic, with the cases, searches and notes the team has gathered, visible to the named members only.",
				"People can add to it, and it keeps a history of who added what.",
			], "Setting up a folder for a section 34 hearing, adding ten cases and giving two colleagues access.",
			"Not built. The Workbench holds one person’s pinned decisions and notes.",
			"Accounts, folders with members and a decision on where the data is hosted."),
			("annotations", "Annotations in cases", "planned", [
				"Highlight a passage in the reader, write a note, and choose whether it is private or shared with the team. The note stays attached to that paragraph whenever anyone opens the case.",
				"Notes would carry into exports so that the reasoning travels with the citation.",
			], "Highlighting the test in a decision, adding “distinguishable, no notice given”, and having a colleague see it on the same paragraph.",
			"Not built. The Markup Reader in the Development tab is a layout study; it saves nothing.",
			"Accounts and a place to store notes, and the reader changes to show them."),
			("alerts", "Saved searches and alerts", "partly", [
				"Save a search and get a short list of new decisions that match it, with a note when an authority you rely on is later distinguished.",
				"A saved-searches page and a digest builder exist. They are early versions, and they depend on the daily intake being scheduled.",
			], "A Monday digest of every new Federal Court decision on section 34, with the Minister’s result on each.",
			"Saved searches and an offline digest builder open from the Development tab.",
			"A scheduled daily intake, owners for saved searches and delivery of the digest in the Workbench or by email."),
			("export", "Export and hand-off", "planned", [
				"Turn a folder into a case list in Word or CSV, or a short issue brief that shows the number of decisions behind every figure.",
				"Exports would carry the source and handling marks, and the date the research was done.",
			], "Exporting a folder as a Word table to attach to a file note.",
			"Not built.",
			"Accounts and folders, plus the handling marks described under Internal documentation."),
			("history", "History and audit", "planned", [
				"A record of what was searched, opened and noted, by whom and when. For a supervisor it shows the research behind a position. For the agency it is part of showing that the system is used properly.",
				"The record would stay inside the agency network.",
			], "Showing that a case was checked for later treatment before it was cited in a factum.",
			"Not built. The live site keeps no record of searches.",
			"Accounts, an audit store and rules on who can read it."),
		],
	},
	"local-ai": {
		"label": "Local private AI",
		"summary": "Optional AI that runs only on the agency’s own computers.",
		"lede": "Normal search in iLit uses no AI, and nothing a person types is sent to an outside AI service. That is a design rule, not a stage in development. This area describes the AI features that could be added on top of it, all assuming the agency can run its own model on its own hardware, and all labelled concept because that model does not exist yet.",
		"why": "AI can help with the things rules handle badly: understanding that two differently worded passages mean the same, or writing a short line about how a case was used. For a litigation division, the condition is that nothing sensitive leaves the building and every AI output can be checked against the source. The design below starts from that condition.",
		"note": "Concept only. Nothing on this page exists on the live site. The live site makes no AI call when someone searches, and an uploaded file is read in memory and not kept.",
		"items": [
			("on-prem-model", "An on-premises model", "concept", [
				"A language model installed on agency computers, used only for the optional features on this page. It would be chosen for being small enough to run on ordinary hardware and good enough on legal text after testing.",
				"Because it runs inside the agency, nothing is sent to an outside provider, and the agency decides when and whether it is switched on.",
			], "A research group asking the model for a one-line summary of a decision, with the question and the answer never leaving the network.",
			"Not set up. No model runs on the live site.",
			"Agency hardware, a choice of model tested on real questions and approval from information security."),
			("data-safety", "Data safety", "concept", [
				"The condition for everything else. Internal documents are stored only on agency servers. The model runs on those servers. Access follows the agency’s own sign-in and every search is logged for audit.",
				"Uploaded files for a one-off check are read in memory and not kept, and every AI-written label is stored as data that links to its source paragraph.",
			], "Showing a privacy officer exactly where each document is stored and who can read it.",
			"The public site makes no AI call on search and reads uploads in memory. The De-identify tool does not keep its key. There is no sign-in, audit log or access control yet.",
			"Sign-in tied to agency accounts, an audit log, a deployment guide for an on-premises or air-gapped install and agency security requirements."),
			("embeddings", "Embeddings and smart search", "concept", [
				"An embedding turns a passage into a list of numbers so passages with similar meaning sit close together. Smart search would let a person ask a question in plain words and get the paragraphs that mean the same, with the reason each matched.",
				"This is paused. A table for paragraph search exists, but no embeddings are live, and the live site does not offer search by meaning.",
			], "Asking “what has the Court said when an officer relies on concerns never put to the applicant?” and getting passages that say “no chance to respond”.",
			"Paused. The table exists; no embeddings are stored.",
			"The on-premises model, computer time to build the index once, and a decision to resume the work."),
			("stored-as-data", "AI work stored as data", "concept", [
				"Wherever AI helps, it would run once, when a decision is added, and the result would be saved: a summary line, a treatment label, a theme. The site then shows the saved result.",
				"That way the site itself stays AI-free, every result can be audited and nobody’s question has to reach a model.",
			], "Reading a saved one-line summary that links to the paragraph it was written from.",
			"Not built.",
			"The on-premises model and a way to record which model and version produced each result."),
			("human-review", "Human review before anything is shown", "concept", [
				"No AI-written label or summary would appear on the site until a sample has been checked by people who know the law. Anything unreviewed would say so.",
				"The review result would be kept with the label, so a reader can see how it was checked.",
			], "A treatment label marked “reviewed on a sample of 200” beside the figure it supports.",
			"An offline trial and a reviewed sample set exist for case outcomes only.",
			"Reviewers, a review procedure and a place to record the result."),
			("hosting", "Where it would run", "concept", [
				"In the short term, a dedicated private computer for the model and a site hosted outside the agency on public law only. In the long term, an internal server inside the agency, with protected data on it.",
				"The right choice depends on what the agency allows, which is why the hosting plan is a decision, not a feature.",
			], "Running the same site on a laptop for a demonstration and on an internal server for real work.",
			"The site runs on one personal computer. There is no backup yet.",
			"A decision on hosting, a backup before anything else, and agency approval of the model hardware."),
		],
	},
}
