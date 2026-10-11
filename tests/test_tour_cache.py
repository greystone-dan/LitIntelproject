import asyncio

from fastapi import FastAPI
from fastapi.testclient import TestClient

from backend.site_tour import tour_steps
from backend.tour_cache import TourCache, TourCacheMiddleware, canonical


def _app(cache):
    app = FastAPI()
    calls = []

    @app.get("/api/citation-intelligence/{case_id}/overview")
    async def overview(case_id: int):
        calls.append(case_id)
        await asyncio.sleep(0.05)
        return {"case": case_id, "n": len(calls)}

    @app.get("/analytics/search/cases")
    async def search(query: str = ""):
        calls.append(query)
        return {"query": query, "n": len(calls)}

    app.add_middleware(TourCacheMiddleware, cache=cache)
    return app, calls


def _cache():
    ids = {spec["citation"]: 100 + k for k, spec in enumerate(tour_steps()["cases"].values())}
    return TourCache(lookup=ids.get), ids


def test_only_the_listed_tour_requests_are_kept():
    cache, ids = _cache()
    app, calls = _app(cache)
    client = TestClient(app)
    vavilov = ids[tour_steps()["cases"]["vavilov"]["citation"]]
    first = client.get(f"/api/citation-intelligence/{vavilov}/overview")
    second = client.get(f"/api/citation-intelligence/{vavilov}/overview")
    assert first.json() == second.json() and second.headers.get("x-tour-cache") == "hit" and calls == [vavilov]
    other = client.get("/api/citation-intelligence/7/overview")       # any other case is never cached
    assert "x-tour-cache" not in client.get("/api/citation-intelligence/7/overview").headers and calls.count(7) == 2
    assert other.status_code == 200
    typed = client.get("/analytics/search/cases?query=anything+a+visitor+types")
    assert "x-tour-cache" not in typed.headers


def test_the_tour_searches_match_however_the_query_is_written():
    listed = [u for u in tour_steps()["cache"] if u.startswith("/analytics/search/cases")]
    assert listed
    path, _, query = listed[0].partition("?")
    reordered = "&".join(reversed(query.split("&")))
    assert canonical(path, query) == canonical(path, reordered)


def test_a_request_already_running_is_shared():
    cache, ids = _cache()
    app, calls = _app(cache)
    vavilov = ids[tour_steps()["cases"]["vavilov"]["citation"]]

    async def both():
        import httpx

        transport = httpx.ASGITransport(app=app)
        async with httpx.AsyncClient(transport=transport, base_url="http://t") as client:
            return await asyncio.gather(*[client.get(f"/api/citation-intelligence/{vavilov}/overview") for _ in range(3)])

    answers = asyncio.run(both())
    assert calls == [vavilov] and len({a.text for a in answers}) == 1


def test_no_database_means_no_cache():
    def broken(_citation):
        raise RuntimeError("no database")

    app, calls = _app(TourCache(lookup=broken))
    client = TestClient(app)
    client.get("/api/citation-intelligence/1/overview")
    client.get("/api/citation-intelligence/1/overview")
    assert calls == [1, 1]
