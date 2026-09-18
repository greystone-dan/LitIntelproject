# External Copilot Review Request

## Task

Review the V1.1 deterministic Discussion Unit and sub-theme analysis for case 677.
Assess whether the output is faithful to the source text, useful as a low-trust
human review aid, and safe to continue improving.

## Read first

Open `SOURCES.md`, then read the complete V1.1 Markdown packet listed there.
Do not rely on an excerpt, and do not use the superseded non-V2 packet.

## Review questions

1. Which sub-themes are coherent argument units, and which are merely contiguous?
2. Which role observations are false positives, weakly supported, or ambiguous?
3. Are metadata, heading, judgment, certification, record, and solicitor spans handled correctly?
4. Are party-position, disposition, and counterargument/limitation cues precise?
5. Do raw and display key terms help without deleting evidence?
6. Do explanations describe the actual issue, actor, assertion, rule, application, or outcome?
7. Are source chunk IDs, offsets, paragraph ranges, and hashes visibly trustworthy?
8. What are the three highest-value deterministic improvements for the next iteration?

## Constraints

- Treat the source section text and evidence contexts as ground truth.
- Do not invent legal conclusions or silently correct the source.
- Do not recommend embeddings, clustering, opaque labels, or runtime activation unless a deterministic fix cannot address the problem.
- This is a read-only staged artifact. Do not edit code, source packets, or canonical data.
- Distinguish false positives, false negatives, granularity problems, explanation problems, and data-integrity problems.

## Required response structure

Use these headings:

1. Executive verdict
2. Strongest observations
3. Weakest observations
4. Sub-theme coherence
5. Role precision
6. Explanation quality
7. Provenance and integrity
8. Prioritized deterministic improvements
9. Residual uncertainty

For every concrete finding, identify the sub-theme or evidence cue and quote the
relevant context. Save the complete response as `RESPONSE.md` in this folder.
