"""Coming soon: the long page on the argument-breakdown work ("Whose position").

Served at ``/coming-soon/argument-breakdown``. It reuses the Coming soon page frame so it
reads like the other pages. Everything here is a preview or concept; the figures are early
tests graded by Claude, not by lawyers, and the page says so.
"""

from __future__ import annotations

# Each section: (anchor, heading, [paragraphs]); a paragraph starting with "- " groups into a list.
_SECTIONS = [
	("problem", "The problem", [
		"A decision is not one voice. A single paragraph may be the judge speaking, the applicant’s argument being summarised, the respondent’s answer, the Board’s earlier finding, or a witness’s evidence. Read quickly, it is easy to take a party’s argument for the Court’s holding, and that is how a case gets cited for something it did not decide.",
		"Counsel also want the next step: given an argument I am about to make, has it been tried, in front of whom, and what happened to it? Today that means reading many decisions and keeping the scorecard in your head.",
	]),
	("others", "What others have tried", [
		"This is a summary of published work and of what the paid tools do. I read abstracts and summaries, not every full paper, so treat the numbers as pointers to check, not as quotations.",
		"- Rhetorical roles. The LegalEval shared task (SemEval-2023) labelled each sentence of a court judgment with one of 13 roles, such as facts, arguments by petitioner, arguments by respondent, analysis and conclusion. The best systems were trained classifiers scoring roughly 76 to 86 on a standard measure, and the task is subjective even for people.",
		"- Argument mining. Researchers have labelled premises, conclusions and their links in European Court of Human Rights decisions, on collections of a few dozen to a few hundred decisions. One finding is that generic labels flatten how legal reasoning really works, and that small, specially trained models often beat general chat models at labelling a given passage.",
		"- Issue-first summaries. Work on Italian courts and in legal benchmarks splits a decision into issues first and then summarises each one. Reviewers preferred this to one long summary, and it keeps long decisions from losing their middle.",
		"- Long documents. Studies find that models tend to leave important material out more often than they invent it, and that quality falls as a decision gets longer. Checking each claim against a quoted sentence in the text helps.",
		"- Citators. Westlaw and Lexis flag how later decisions treated a case, as part of paid subscriptions the Division does not hold. They follow a case through its citations. They do not tell you whose position a paragraph reports, or match your draft argument to decided issues. I found no Canadian tool that does either for immigration law.",
		"What I took from this: label who is speaking first, work issue by issue, tie every label to a paragraph and a quote, and measure against people’s judgement instead of trusting a model’s confidence.",
	]),
	("approach", "Our approach", [
		"The work is built as layers, each one checkable on its own.",
		"- Holder and layer. Every paragraph is tagged with whose position it reports and at which layer it sits: (1) the judge, (2) the parties’ submissions to this court, (3) the earlier decision-maker, (4) a first-instance party’s position reported inside that decision, (5) a witness or document, (6) the legal framework or prior authority.",
		"- A fixed case frame. The court, the type of case, the parties and the side each one is on come from fixed rules over the header and the style of cause, not from a model. The same decision always gets the same frame.",
		"- Fixed rules first. Cue phrases such as “the applicant submits”, “I am not persuaded” and “the Board found” settle many paragraphs with the triggering phrase shown beside the tag. A model is used only to read what the rules cannot.",
		"- An issue map. The issues the Court actually decides, in order, each with its disposition (allowed, dismissed, partly allowed, found harmless, not decided), and the party points the Court answered one by one.",
		"- Matching a draft to decided issues. The end goal is Live Analysis: you paste a one-sided draft argument and see, for each point, the decided issues it resembles and what happened to them, with the supporting paragraph one click away.",
		"The design rule stays the same as for the rest of the site. AI is used only when public case law is added to the library, and what it finds is stored as data that points back to the source paragraph. Searching and reading make no AI call, and nothing a person types or pastes is sent to a model by default.",
	]),
	("results", "Results so far, with the caveats", [
		"These are early tests on a small graded sample. The grading was done by Claude readers, not by lawyers, and no lawyer has reviewed the sheets yet. Please read the figures as indications.",
		"- Whose position. On the graded sample the holder was right about 8 times in 10.",
		"- Issue results. The result of an issue (who won it) was right about 88% of the time.",
		"- The readers disagreed less with each other than with the first AI pass: two independent Claude readers agreed on about 9 paragraphs in 10, which is why the fixed rules and a second reading are used as checks.",
		"- Known problems. Memoranda and written submissions can be mistaken for decisions. In split Supreme Court decisions the dissent can be reported as the holding. Paragraphs where the rules cannot tell are shown as “not yet detected” instead of guessed.",
		"A reader preview, “Show whose position”, already runs on about 660 decisions. It carries a Preview label and will keep it until lawyers have checked a sample.",
	]),
	("next", "What is next", [
		"- Fix the known errors above, starting with memoranda and split decisions.",
		"- Add the issue map, with the result per issue and the Court’s answer to each party point.",
		"- A check of a sample by lawyers before any figure is quoted as accuracy, and before the Preview label is removed.",
		"- Extend from about 660 decisions to the library, and to French decisions.",
		"- Live Analysis: match a draft argument to decided issues using fixed rules over stored data. Anything that needs a language model to write a summary waits for the on-premises model.",
	]),
]


def body(e) -> str:
	"""HTML body for the page; ``e`` escapes text."""
	out = (
		'<header><p class="eyebrow">Coming soon · New features</p><h1>Whose position: breaking a decision into arguments</h1>'
		'<p class="lede">A preview of work in progress. Each paragraph of a decision would show whose position it reports, so you can tell the Court’s own reasoning from a party’s argument, and in time check a draft argument against how the same issues were decided.</p>'
		'<div class="note"><strong>Concept and preview.</strong> Only the reader preview exists today, on about 660 decisions. The accuracy figures on this page come from early tests graded by Claude, not by lawyers.</div></header>'
		'<nav class="pager" aria-label="On this page">'
		+ "".join(f'<a href="#{a}">{e(h)}</a>' for a, h, _ in _SECTIONS)
		+ "</nav>"
	)
	for anchor, heading, paras in _SECTIONS:
		out += f'<section id="{anchor}"><h2>{e(heading)}</h2>'
		items = []
		for text in paras:
			if text.startswith("- "):
				items.append(f"<li>{e(text[2:])}</li>")
				continue
			if items:
				out += f'<ul>{"".join(items)}</ul>'
				items = []
			out += f"<p>{e(text)}</p>"
		if items:
			out += f'<ul>{"".join(items)}</ul>'
		out += "</section>"
	out += (
		'<nav class="pager"><a href="/data-explorer?tab=roadmap-intelligence&amp;group=roadmap" target="_top">&larr; Increased intelligence</a>'
		'<a href="/data-explorer?tab=roadmap-overview&amp;group=roadmap" target="_top">All areas</a></nav>'
	)
	return out
