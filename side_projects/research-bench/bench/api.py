"""Web API route outline. Framework-neutral; map each route to a service call.

GET    /bench                         LibraryService.my_bench(user)
POST   /bench                         LibraryService.save(user, decision, folder, tags)
POST   /bench/{case_id}/notes         LibraryService.add_note(...)
POST   /bench/{case_id}/publish       LibraryService.publish_to_team(...)
GET    /library?tag=                  LibraryService.team_library(tag)

GET    /decisions/{citation}/annotations    AnnotationService.for_decision(...)
POST   /decisions/{citation}/annotations    AnnotationService.annotate(...)
POST   /annotations/{id}/replies            AnnotationService.reply(...)

POST   /search                        SearchService.run(user, query)
GET    /search/recent                 SearchService.recent(user)
POST   /search/alerts                 SearchService.create_alert(user, query)
POST   /search/alerts/{id}/run        SearchService.rerun(alert)

GET    /tracker                       CaseTrackerService.my_list(analyst)
POST   /tracker                       CaseTrackerService.track(analyst, docket, style)
POST   /tracker/check                CaseTrackerService.check(analyst)

POST   /analysis                      AnalysisService.analyse(user, citation, provision, question)

Auth: every route resolves `user` from the session. Team routes also check team
membership. Not built yet.
"""
