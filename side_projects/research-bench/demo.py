"""End-to-end run of the Research Bench skeleton: python3 demo.py"""
from datetime import date

from bench.adapters import StubCaseLawAdapter, StubDocketAdapter
from bench.models import Label, Scope, SearchQuery
from bench.seed import DECISIONS, DOCKETS
from bench.services import (AnalysisService, CaseTrackerService, AnnotationService, LibraryService,
                            PublishBlocked, SearchService)
from bench.store import InMemoryStore

store = InMemoryStore()
lib = LibraryService(store)
ann = AnnotationService(store)
search = SearchService(store, StubCaseLawAdapter(DECISIONS))
act = CaseTrackerService(store, StubDocketAdapter(DOCKETS))

me, colleague = "daniel", "analyst2"

hits = search.run(me, SearchQuery("non-refoulement"))
print("Search 'non-refoulement':", [d.citation for d in hits])
saved = search.create_alert(me, SearchQuery("non-refoulement"))
search.rerun(saved)

wahab = lib.save(me, hits[0], folder="Wahab", tags={"art33", "s34"})
lib.add_note(me, wahab, "Leaves the 'how' to the ID.", paras=[121])
lib.publish_to_team(me, wahab)
lib.add_note(colleague, wahab, "Pair with Mason on interpretation vs. application.")
print("Team library:", [(c.decision.citation, len(c.notes)) for c in lib.team_library()])

blocked = lib.save(me, hits[1], tags={"protected-b"})
try:
    lib.publish_to_team(me, blocked)
except PublishBlocked as e:
    print("Publish blocked:", e)

a = ann.annotate(me, "2026 FCA 140", 124, 124, Label.SUPPORTS,
                 "Art 33 considered in interpreting the ground.", Scope.TEAM)
ann.reply(colleague, a, "Agree; cite with 106-108.")
print("Annotations on Wahab:", [(x.para_from, x.label.value, len(x.replies))
                                for x in ann.for_decision("2026 FCA 140", colleague)])

act.track(me, "A-000-26", "Example v. Canada (MCI)")
act.track(me, "A-001-26", "Example 2 v. Canada (MPSEP)")
for m in act.my_list(me):
    m.last_seen = date(2026, 9, 20)
alerts = act.check(me)
print("New FCA activity:", [(x.docket, x.entry.text) for x in alerts])
print("Second check (should be empty):", act.check(me))
print("Recent searches:", [r.query.text for r in search.recent(me)])
print("Live analysis (stub):", AnalysisService(store, search.source).analyse(me, "2026 FCA 140", "s. 34(1)(f)"))
