# Task: Reframe roadmap around demo product usability

Status: complete
Created: 2026-09-22
Updated: 2026-09-22

Task: Rework the product roadmap from corpus-quality-first delivery to a demo-first product plan centered on usability, issue/type case discovery, evidence-led reading, and a coherent research journey.
Why now: The deterministic research foundation and active Data Explorer exist; the near-term goal is to demonstrate product functionality clearly before resuming broad data-quality work.
Owner surface: `ROADMAP.md`, with supporting alignment in `docs/RESEARCH_UI_GUIDE.md` and `CHANGELOG.md` if needed.
Dependencies: Existing `/data-explorer` search, reader, evidence layers, case summary, legal themes/statutes, citation intelligence, and current issue/type metadata.
Risk boundary: Do not discard data-quality work; defer it explicitly. Keep only demo-safety fixes active where missing or misleading evidence would harm the demo.
Smallest falsifiable check: The revised roadmap names one primary issue-to-case-to-evidence journey, prioritizes issue/type discovery and usability, and places corpus-quality work in a later track with measurable demo acceptance criteria.
Acceptance criteria:
- ROADMAP.md has a demo-product objective and audience/jobs.
- Issue/type discovery is the first implementation priority.
- Usability, reader continuity, and demo validation have explicit phases.
- Data quality, authority coverage, and corpus hardening are explicitly deferred rather than removed.
- Demo acceptance criteria include curated scenarios, source traceability, responsive usability, and no manual database intervention.
Docs/generated references: `ROADMAP.md`; preserve `SYSTEM_REFERENCE.md` as current-state authority.
Rollback/recovery: Restore the prior roadmap sections from git if the product direction changes; no code or database changes are required.
Evidence: Read-only roadmap review completed. Replaced the quality-first roadmap with a demo-first sequence: Priority 0 issue/type discovery, Priority 1 coherent research journey, Priority 2 usability and reader polish, Priority 3 evidence-led demo packaging. Preserved corpus quality, authority coverage, and advanced intelligence as an explicitly deferred track with demo-safety exceptions. Updated `ROADMAP.md` on 2026-09-22.
Residual risk: The roadmap is now aligned to product direction, but issue/type entry points, curated cohorts, and browser checks still need implementation.
Commit allowed: yes
Push allowed: yes
