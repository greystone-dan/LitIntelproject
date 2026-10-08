"""Words for the Coming soon pages.

Each item: (anchor, title, status, [paragraphs], example, today, needs[, elsewhere]).
The optional last field says, factually, what existing tools offer for the same need.
Statuses are honest: built, partly, progress, planned, concept. Nothing here needs AI
when someone uses the site; where AI appears it is optional, on the agency's own
computers, and its output is stored as data that points back to the source text.
"""

from __future__ import annotations

# Three kinds of work: data steps that improve every page, new features, and the groundwork an
# agency deployment would need. Within each part the areas run from closest to furthest out.
PARTS = [
	("data", "Better data", "Data steps: making the library more accurate and more complete. They add no new screens, but every search, statistic and link gets better.", ["accuracy", "expansion"]),
	("features", "New features", "New things you could do on the site, built on that data.", ["intelligence", "fc-files", "team"]),
	("agency", "Ready for the agency", "What a deployment inside the Agency would need: approvals and hardening, the Division’s own documents, and AI that runs only on agency computers.", ["readiness", "internal", "local-ai"]),
]

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
				"A separate check that flags short-form links pointing at the wrong case, for example a capitalised word such as “Lake” taken for a case name, is built and held back until the rebuild.",
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
				"A second-opinion check is also built for use when decisions are added: a small model reads the end of a decision and must quote the sentence it relied on. Its answer is stored apart and never replaces the rule result; it only flags decisions for a second look.",
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
				"A shared name list merges initials, titles, French forms and surname-only mentions, so a profile can show every other name a judge appears under. Every merge can be undone.",
			], "Opening a judge profile and trusting that it holds that judge’s decisions and only theirs.",
			"Judge Profiles are live. Many spelling variants are merged. A few wrong merges and several extraction gaps remain.",
			"Pruning the wrong merges, extracting names where they are missing, and covering French-language decisions."),
			("parties", "Minister and party names", "planned", [
				"The Minister’s title appears in dozens of spellings and older forms, and some decisions list parties that have nothing to do with immigration. Cleaning these up makes the government-party filter short and reliable.",
				"A draft set of rules maps every variant to one current name and sets aside non-immigration parties. It has not been applied.",
			], "Filtering to decisions against the Minister of Public Safety and getting every one of them, whatever the title was in that year.",
			"The filter works but lists many variants of the same Minister.",
			"Review of the draft rules, then applying them with an undo list."),
			("measuring", "Measuring accuracy", "partly", [
				"Each automated step needs a number that says how good it is. Hand-reviewed sets exist for outcomes, case types and statute references, and small programs score the rules against them.",
				"The next step is a fixed pass mark for each step, checked before any change reaches the site, and a short public note of the latest scores.",
			], "Reading “outcomes: checked against 587 hand-reviewed decisions” beside an outcome statistic, with the date of the check.",
			"Reviewed sets and scoring scripts exist. There are no agreed pass marks and no published scores.",
			"Agreed pass marks per step, a check that runs before each release and a page that shows the results."),
		],
	},
	"expansion": {
		"label": "Expansion",
		"summary": "More cases, more tags, more laws and regulations.",
		"lede": "A library is only useful for the questions it can answer. Today iLit holds decisions of the Federal Court, the Federal Court of Appeal, the Supreme Court of Canada and the Refugee Protection Division, with the Refugee Appeal Division being added. This area is about widening that coverage and keeping it current, without lowering the quality bar set by the accuracy work.",
		"why": "Counsel working a file rarely stops at one court. A judicial review of a refugee decision depends on the tribunal’s own decisions, the Court’s case law and the statutes behind both. The more of that sits in one searchable place, the less time is spent hunting across websites.",
		"items": [
			("more-cases", "More cases", "progress", [
				"Refugee Appeal Division decisions are being loaded, and Refugee Protection Division decisions after 2020 are being added from the Refugee Law Lab’s open collection. Each decision keeps a link to its original source.",
				"New decisions go through the same reader, citation and statute tools as the rest of the library, so a larger library does not mean a different experience.",
			], "Checking how the Refugee Appeal Division has treated a credibility finding, then following a Federal Court review of the same decision.",
			"Federal Court, Federal Court of Appeal, Supreme Court and Refugee Protection Division are in. Refugee Appeal Division loading is under way.",
			"Finishing the loads, checking case types and names on the new decisions, and recording where each batch came from."),
			("daily-intake", "Keeping the library current", "partly", [
				"New Federal Court decisions are published every day. A daily intake job finds them, downloads them and adds them to the library, running the same checks as the original load.",
				"The job is built and has been run by hand. A scheduler and an installer for it are written too, but it is not switched on, because scheduling it needs sign-off on the computer that runs the site.",
				"Some tidy-up steps, such as case types and judge names, are not yet run on newly added decisions; they are applied in batches.",
			], "A decision released this morning being searchable by the afternoon, without anyone running a script.",
			"Built and tested, but run by hand and not scheduled.",
			"Sign-off to schedule it, a quiet failure alert so a missed day is noticed, and a short log of what each run added."),
			("more-tags", "More tags", "planned", [
				"Tags describe what a decision is about: the legal issues, the grounds raised, the statute sections applied. They drive filters, statistics and “find similar” features.",
				"The current tag set works, and the rules that produce it are fixed and inspectable. A wider set would let searches go deeper, for example by naming the specific ground of inadmissibility or the type of procedural fairness complaint.",
				"Candidates already drafted include detention grounds (danger, flight risk, identity), findings such as a negative credibility finding or fettering of discretion, and the type of removal order.",
			], "Finding every decision on a particular ground of inadmissibility and comparing outcomes by year.",
			"A working tag set exists, with filters and statistics built on it.",
			"Agreement on the list of new tags, rules for each, and a check against hand-graded decisions before any is shown."),
			("laws-regulations", "More laws and regulations", "partly", [
				"Decisions rely on statutes, regulations and sometimes ministerial instructions. The library holds the main federal immigration instruments so that a section cited in a decision can be read in place.",
				"Next in line are the other federal instruments immigration counsel cite, such as the Customs Act, the Canada Border Services Agency Act and the rules of each Board division, plus the repealed Immigration Act for older decisions.",
				"Code to show the version of a section that was in force on the date of a decision is written; how many past versions are stored is still being checked. Quebec, Civil Code and most provincial material is left out for now, by decision.",
			], "Opening a cited regulation section from the reader and seeing the wording, plus every decision that cites it.",
			"A federal statute library exists, with a few provincial acts. Quebec, British Columbia and Saskatchewan statutes are left out by decision.",
			"Importing the remaining federal instruments, filling in past versions, and a decision on policy materials such as program instructions."),
			("fc-record", "Reading more of the Federal Court record", "partly", [
				"The Court’s record of each immigration case is free text. Fixed rules already turn most entries into steps such as leave granted or judicial review dismissed.",
				"Gaps remain: many cases have no clear subject, and the time from filing to removal, the destination of a removal and the outcome of a stay are only sometimes read correctly.",
			], "Seeing how long stay motions take to be decided, by year, with every figure counted from the record.",
			"Federal Court Analytics is live on the classified entries. Subjects and removal details are sparse.",
			"Better rules for subjects and removal details, checked against hand-read files, then a re-run over every case."),
			("french", "French-language counterparts", "planned", [
				"A few hundred French-language decisions are in the library, mostly Federal Court. Each decision is stored in one language, so an English decision’s French counterpart is not linked to it.",
				"Counsel working in French, or comparing the two versions of a decision, would need both stored and joined.",
			], "Opening a decision and switching to its French version at the same paragraph.",
			"Some French decisions are stored. None from the Refugee Appeal Division or Refugee Protection Division. No counterpart linking.",
			"Scoping which decisions have French counterparts, storing both languages, and linking paragraph to paragraph."),
			("id-iad", "Immigration Division and Immigration Appeal Division", "concept", [
				"Decisions of the Immigration Division and the Immigration Appeal Division are not published in the datasets used so far, so the library holds none of them. For hearings work this is the largest gap.",
				"Closing it depends on a lawful source and terms of use, not on technology. Routes identified so far: asking the open research groups that already republish Board decisions, asking the Agency what it holds as a party, or a licence. Copying them from a site whose terms forbid it is ruled out.",
				"Once a source exists, the import needs very little new work: the same reader, citation and tagging steps apply.",
			], "Reading an admissibility decision next to the Federal Court judicial review of it.",
			"None are held.",
			"A confirmed source, terms of use and privacy approval, then the same import and tagging as other decisions."),
		],
	},
	"fc-files": {
		"label": "Federal Court files",
		"summary": "Following live Federal Court immigration files.",
		"lede": "iLit already holds the Federal Court’s public record for every immigration case, and Federal Court Analytics adds it up. The next step is to use the same record for the files the Division is working on today: follow them, see when they move, and keep deadlines next to them.",
		"why": "Checking a file today means opening the Court’s website and looking it up by number, one file at a time. A list that shows every followed file, with a flag when something new is recorded, saves that routine and makes it harder to miss a step.",
		"items": [
			("fc-analytics", "Federal Court Analytics", "built", [
				"Charts and tables over the whole immigration record: how cases progress, leave and judicial review outcomes by year, the time between steps, motions by type, judges, counsel and the registry.",
				"Every figure is counted from the record, so it includes the cases that end without a published decision, which are most of them.",
			], "Seeing the leave rate for a year and how long leave decisions took, counted over every file and not a sample.",
			"Live on the site.",
			"Better reading of subjects and removal details (see Expansion), and a scheduled intake so the record stays current.",
			"The Court publishes overall totals each quarter. I found no other tool with these figures for every immigration file."),
			("fc-follow", "Follow a file", "partly", [
				"Paste a list of file numbers, or text that contains them, and follow those files in the Workbench. Each shows its steps so far, with a flag when the stored record has moved since you last looked.",
				"Files can be grouped and tagged, and the list downloads as a spreadsheet.",
			], "Opening the Workbench on Monday and seeing that three of your forty files had something new recorded last week.",
			"Built in the Workbench and labelled Coming soon. The record it reads is only as fresh as the last intake.",
			"A scheduled intake, then accounts so each person keeps their own list.",
			"The Court’s website looks up one file at a time and gives no notice when a file moves."),
			("fc-deadlines", "Deadlines", "partly", [
				"Attach a deadline and a label to a followed file and see what is due or overdue in the next week or month on the Workbench home.",
			], "Seeing at a glance that a reply is due in four days on one file and overdue on another.",
			"The storage and the summary are built. The Workbench card is labelled Coming soon.",
			"Finishing the card, and later working out common deadlines from the record itself, with a person confirming each one."),
			("fc-collection", "Always-on collection", "planned", [
				"New entries on the Court’s record are collected by a program that is started by hand today. Running it on a separate, always-on worker would keep the record current without anyone starting it.",
				"It spaces out its requests and stops if the Court’s site asks for human verification.",
			], "A file’s new hearing date appearing in the Workbench the next morning.",
			"The collector exists and is run by hand.",
			"Approval to run the worker, a place to run it, and a notice when a run fails."),
		],
	},
	"readiness": {
		"label": "Government readiness",
		"summary": "What an approval inside the agency would ask for.",
		"lede": "Before any government team relies on a tool, security, privacy and accessibility reviews ask the same questions: where the data lives, who can reach it, what is logged, what happens if the machine fails, and whether everyone can use it. This area lists what is ready for those reviews and what is not.",
		"why": "A pilot that meets these requirements from the start can be approved in weeks rather than months. The simplest first step is a version that holds public case law only, with document upload switched off, so the review is light.",
		"note": "These items are groundwork, not features. The Agency decides what its reviews require; nothing here claims an approval.",
		"items": [
			("review-pack", "Review documents", "partly", [
				"Plain documents a security or privacy reviewer would ask for: what data is held and how sensitive it is, how it flows, which outside services are used, what is logged and for how long, inputs for a privacy impact assessment, and a statement on how AI is and is not used.",
				"The privacy impact assessment itself would be run by the Agency.",
			], "Handing a reviewer one folder that answers their first twenty questions.",
			"First versions are written and kept with the code.",
			"Checking them against the live computer, and the Agency’s own templates."),
			("public-only", "A public-law-only version", "planned", [
				"One switch that turns off document upload and Live analysis, so the site holds and handles public case law only. It is the lightest thing to approve.",
			], "Running a pilot for the Division in which nothing but published decisions ever touches the site.",
			"Not built. Uploads are read in memory and never kept, but the feature is on.",
			"The switch, and a page that says plainly which version is running."),
			("hosting", "Where it would run", "planned", [
				"In the short term, a dedicated computer for the model and a site hosted in Canada on public law only. In the long term, an internal server inside the agency, with protected data on it, assessed to the government’s Protected B standard.",
				"The right choice depends on what the agency allows, which is why the hosting plan is a decision, not a feature.",
			], "Running the same site on a laptop for a demonstration and on an internal server for real work.",
			"The site runs on one personal computer through a secure connection service.",
			"A decision on hosting and agency approval of the hardware."),
			("backups", "Backups and recovery", "planned", [
				"Regular copies of the database, a tested way to restore them, and a stated time to recover after a failure.",
			], "Replacing a failed computer and having the site back the same day.",
			"There is no backup yet. This comes before any wider use.",
			"A first full backup, a schedule, and a restore test."),
			("accessibility", "Accessibility", "partly", [
				"Meeting the web accessibility standard the government uses (WCAG 2.1 AA): keyboard use, screen readers, contrast, and text alternatives for charts and maps.",
			], "A colleague who uses a screen reader working through a search and a decision without help.",
			"A first review and some fixes are done. No keyboard or screen-reader testing yet.",
			"Automated checks on every page, a test with a screen reader, and a published accessibility statement."),
			("french-ui", "French interface", "planned", [
				"Every label, button and page available in French, with a language switch. This is separate from French decisions, described under Expansion.",
			], "Using the whole site in French.",
			"English only.",
			"Moving the interface text into translation files and a reviewed translation."),
			("hardening", "Security hardening", "partly", [
				"The usual protections for a government web service: strict browser security settings, fonts and scripts served from the site itself rather than outside services, limits and scanning on uploads, and checks on the software it depends on.",
			], "A security scan of the site coming back clean.",
			"Upload size limits and automatic dependency checks exist. Browser security settings and self-hosted fonts do not.",
			"Adding the missing settings, serving all files locally, and a named person who applies security updates."),
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
			"Live Analysis reads an uploaded file in memory, lists its cases and statutes and keeps nothing. When the file is itself a decision, it also reads its court, date, outcome and type with the same fixed rules.",
			"A way to identify arguments without sending text outside the agency, and lawyer review of the suggestions on real memoranda."),
			("memo-check", "Memo citation check and gap check", "partly", [
				"A citation check lists the authorities a memo cites, shows how each has since been treated, and flags those that look overturned or questioned. A gap check suggests commonly cited authorities on related issues that the memo does not mention.",
				"Early versions exist. The gap check works on decisions already in the library, not on uploaded briefs.",
			], "Running a draft factum through the check the day before filing and finding a case that was overturned last year.",
			"Early versions exist in the development area, outside the main site.",
			"Reliable treatment labels (see Increased intelligence) and a version that works on uploaded documents without storing them.",
			"Citation checkers come with paid services the Division does not hold. CanLII has no such check."),
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
			("citation-treatment", "Citation treatment", "partly", [
				"Treatment says how a later decision used an earlier authority: followed, applied, distinguished, questioned or criticised. Shown beside each citing paragraph, with a warning when the tide turns, it replaces manual citation checking.",
				"A first rule-based version sorts citing paragraphs into a few broad kinds, and a batch job records, for each paragraph of a decision, which later cases cite it and the phrase they used: “applied in”, “see also”, “distinguished”. Neither is shown on the main site yet.",
				"A yellow warning for cases affected by a later development, such as a decision later overturned, was built from a short reviewed list and then switched off until the list can be kept complete.",
			], "Opening a leading case and seeing that it was followed in most later decisions but distinguished in the last three, each linked to its paragraph.",
			"Citation Intelligence is live: who cites a case, how that changed over time and the outcomes of the citing decisions. The paragraph-level record and first labels exist outside the main site.",
			"Labels assigned per citing paragraph with a visible “how assigned” line, review of a sample by lawyers, and refined citation links underneath.",
			"Westlaw and Lexis flag later treatment as part of paid subscriptions, which the Division does not hold. I found no treatment flags in CanLII."),
			("citation-enhancements", "AI-backed citation enhancements", "concept", [
				"On top of the rule-based links, an on-premises model could write a plain-language line saying why a case was cited, or flag a citation whose treatment is unclear.",
				"The line would be written once, when the decision is added, and stored with a link to the paragraph it summarises. Nobody’s search would be sent to a model.",
			], "Reading a list of citing paragraphs with a one-line reason for each, and clicking through to confirm it.",
			"Not built. There is no model installed.",
			"The on-premises model (see Local private AI), reviewed examples to test it against, and a rule that anything unreviewed is labelled as such."),
			("discussion-units", "Discussion units and argument subsections", "partly", [
				"A decision is long, but it has a shape: the facts, the legal test, the analysis, the disposition. Discussion units mark those parts and the argument subsections inside them, so a search can land on the part that states the test.",
				"A rule-based version has been built and tested in a sandbox. It is not yet stored in the database.",
				"Later, each argument could carry its own result, succeeded, failed or not reached, so a search can find where a particular argument worked, not only cases the applicant won.",
			], "Searching “test for reasonable apprehension of bias” and landing on the paragraphs that state the test, not on a passage that merely mentions it.",
			"The outline of headings is live in the reader. Discussion units run in a testing page and as reports.",
			"Review of the unit boundaries against a hand-checked set, then storing units when decisions are added and search by unit."),
			("themes", "Themes", "partly", [
				"Themes group the arguments that recur across decisions, such as the recurring complaints about credibility findings or about reasons for a refusal, and show which statutory provisions each one leans on.",
				"A first Legal Themes page exists. It is built on tags and will be sharper once discussion units are stored.",
			], "Seeing the three most common ways applicants attack a credibility finding, with a sample decision for each.",
			"A Legal Themes and Statutes page exists in the development area, outside the main site.",
			"Stored discussion units, better tags and a plain-language label for each theme."),
			("authority-trends", "Authority trends", "partly", [
				"Across the whole library, sort authorities into emerging, dominant and declining, spot decisions on their way to becoming leading cases, and notice when one authority replaces another on an issue.",
				"The same work shows how an authority moves between courts, from the Federal Court to the Court of Appeal and the Supreme Court, and finds indirect chains where one case relies on another through a third.",
			], "Seeing that a leading case on a ground has been cited less each year since a newer Court of Appeal decision, which now carries the issue.",
			"The calculations are built and can be downloaded as spreadsheets. No page on the site shows them yet.",
			"A page that shows them plainly, cleaner citation links underneath, and a check of the labels by a lawyer.",
			"I found no Canadian tool that tracks immigration authorities this way. Paid services show citing cases one authority at a time."),
			("neighbourhoods", "Citation neighbourhoods", "partly", [
				"Start from one case and see what it relies on, what cites it and what is cited alongside it, grouped by issue. Compare two cases and see the authorities they share.",
				"The Citation Map page does the first part today, and a Case Compare page puts two decisions side by side. Grouping by issue and showing neighbourhoods inside the reader come next.",
			], "Starting from a leading decision and finding the other authorities that are always cited with it.",
			"A Citation Map page exists in the development area, outside the main site.",
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
				"Next is the judge’s Federal Court docket record beside the decisions: leave, judicial review and stay motions, with a warning when the number is small.",
			], "Checking how often a judge has ruled for the Minister on procedural fairness, and seeing that the figure rests on twelve decisions.",
			"Judge Profiles are live with counts and unclassified decisions shown, and two judges can be compared on one issue.",
			"Finished name cleanup, extraction where names are missing and outcome accuracy close to complete before any rate is quoted.",
			"LexisNexis Context studies the language judges use. I found no tool that counts Federal Court immigration outcomes by judge."),
			("case-at-a-glance", "Case at a glance", "partly", [
				"A compact card at the top of each decision: the issue and type of case, the outcome, the sections applied, and a short summary made of the decision’s own holding paragraph, chosen by rule.",
				"Because the summary is the court’s own words, it can always be traced back, and nothing is written by AI.",
			], "Opening ten search results and knowing in a few seconds which three are worth reading in full.",
			"The card and the rule-based summary are built and hidden behind the reader’s “Show experimental” switch.",
			"A check of the chosen paragraphs on a sample, then switching the card on.",
			"CanLII shows short AI-written summaries for some areas of law. These would be the court’s own words, picked by rule."),
			("passage-search", "Search by passage, without AI", "partly", [
				"Type a sentence and get the paragraphs that say it, across the whole library. A hand-reviewed list of immigration terms widens the search, so “doctor” also finds “physician” and “psychologist”.",
				"Search operators already work for those who want them: AND, OR, NOT, and filters such as court:, year: and judge: typed in the box.",
			], "Typing “officer relied on extrinsic evidence without notice” and getting the paragraphs where judges discuss exactly that.",
			"A passage search page and the term list exist in the development area. The full paragraph index is not yet built on the live library.",
			"Building the paragraph index on the site computer, and tuning the ranking on a set of real research questions.",
			"CanLII Search+ answers plain-language questions using hosted AI. This would do it with fixed rules, and nothing typed would leave the site."),
			("show-your-work", "Showing how each label was assigned", "planned", [
				"Next to a case type, an outcome, a tag or a link, the site would show in plain words how it was decided: which rule fired and which words in the decision triggered it.",
				"This matters because a label you cannot check is a label you cannot rely on in front of a tribunal or a supervisor.",
			], "Clicking an outcome label and seeing the sentence in the decision that produced it.",
			"Some labels already link back to their source text. There is no common “how assigned” line.",
			"Recording the reason at the time each label is made, and a small design for showing it without clutter."),
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
				"On an agency network the sign-in would use the agency’s own accounts and multi-factor login, so nobody has to create a new password.",
			], "Signing in and finding your saved searches and pinned cases exactly as you left them.",
			"No sign-in. A single shared site password is built and switched off. The Workbench has a demo mode where a typed name picks a private bucket.",
			"A deployment where real sign-in makes sense and a decision on roles."),
			("teams", "Teams and shared folders", "planned", [
				"A team folder for a file or a topic, with the cases, searches and notes the team has gathered, visible to the named members only.",
				"People can add to it, and it keeps a history of who added what.",
			], "Setting up a folder for a section 34 hearing, adding ten cases and giving two colleagues access.",
			"Not built on the site. The Workbench holds one person’s pinned decisions and notes, and a team workspace prototype exists in the testing area.",
			"Accounts, folders with members and a decision on where the data is hosted."),
			("annotations", "Annotations in cases", "planned", [
				"Highlight a passage in the reader, write a note, and choose whether it is private or shared with the team. The note stays attached to that paragraph whenever anyone opens the case.",
				"Notes would carry into exports so that the reasoning travels with the citation.",
			], "Highlighting the test in a decision, adding “distinguishable, no notice given”, and having a colleague see it on the same paragraph.",
			"Not built. The Markup Reader in the development area is a layout study; it saves nothing, but can already export a decision to Word with margin notes as Word comments.",
			"Accounts and a place to store notes, and the reader changes to show them."),
			("alerts", "Saved searches and alerts", "partly", [
				"Save a search and get a short list of new decisions that match it, with a note when an authority you rely on is later distinguished. For the Division the useful version is outcome-aware: tell me when the Minister loses on an issue I follow.",
				"A saved-searches page and a digest builder exist. They are early versions, and they depend on the daily intake being scheduled.",
			], "A Monday digest of every new Federal Court decision on section 34, with the Minister’s result on each.",
			"Saved searches and an offline digest builder exist in the development area, outside the main site.",
			"A scheduled daily intake, owners for saved searches and delivery of the digest in the Workbench or by email.",
			"myCanLII sends alerts on new matching decisions and new citing cases. These would add the outcome, and the Minister’s side of it."),
			("export", "Export and hand-off", "partly", [
				"Turn a folder into a case list in Word or CSV, or a short issue brief that shows the number of decisions behind every figure.",
				"Much of this exists already: search results download as a spreadsheet or Word file, the Workbench case list and pins download as spreadsheets and print as a brief, and an issue brief page is in the development area.",
				"Exports would carry the source and handling marks, and the date the research was done.",
			], "Exporting a folder as a Word table to attach to a file note.",
			"Search, Workbench and brief exports work. Folder exports and handling marks do not exist.",
			"Accounts and folders, plus the handling marks described under Internal documentation."),
			("history", "History and audit", "planned", [
				"A record of what was searched, opened and noted, by whom and when. For a supervisor it shows the research behind a position. For the agency it is part of showing that the system is used properly.",
				"The record would stay inside the agency network.",
			], "Showing that a case was checked for later treatment before it was cited in a factum.",
			"A basic request log is built and off by default. It records pages, not people or what they searched.",
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
			("on-prem-model", "An on-premises model", "partly", [
				"A language model installed on agency computers, used only for the optional features on this page. It would be chosen for being small enough to run on ordinary hardware and good enough on legal text after testing.",
				"Because it runs inside the agency, nothing is sent to an outside provider, and the agency decides when and whether it is switched on.",
			], "A research group asking the model for a one-line summary of a decision, with the question and the answer never leaving the network.",
			"No model runs on the live site. The switches to use a local model are built and off, and a harness to compare models on fixed test sets exists.",
			"Agency hardware, a choice of model tested on real questions with pass marks set in advance, and approval from information security."),
			("data-safety", "Data safety", "partly", [
				"The condition for everything else. Internal documents are stored only on agency servers. The model runs on those servers. Access follows the agency’s own sign-in and every search is logged for audit.",
				"Uploaded files for a one-off check are read in memory and not kept, and every AI-written label is stored as data that links to its source paragraph.",
			], "Showing a privacy officer exactly where each document is stored and who can read it.",
			"The public site makes no AI call on search and reads uploads in memory. The De-identify tool does not keep its key. A shared password gate and a basic request log are built and off; there is no per-person sign-in or audit.",
			"Sign-in tied to agency accounts, an audit log, a deployment guide for an on-premises or air-gapped install and agency security requirements."),
			("embeddings", "Embeddings and smart search", "concept", [
				"An embedding turns a passage into a list of numbers so passages with similar meaning sit close together. Smart search would let a person ask a question in plain words and get the paragraphs that mean the same, with the reason each matched.",
				"This is paused. A private embedding pipeline that runs on the site computer is written, but the live site does not offer search by meaning.",
			], "Asking “what has the Court said when an officer relies on concerns never put to the applicant?” and getting passages that say “no chance to respond”.",
			"Paused. Code exists; search by meaning is not offered on the site.",
			"The on-premises model, computer time to build the index once, and a decision to resume the work.",
			"CanLII Search+, Westlaw and Lexis offer AI search on their own hosted services. This would run inside the agency."),
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
		],
	},
}
