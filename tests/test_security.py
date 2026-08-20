import time

from backend import main


def test_access_cookie_signature_and_expiry(monkeypatch):
    monkeypatch.setattr(main.time, "time", lambda: 1_000)
    token = f"1000.{main._access_signature('1000', 'secret')}"

    assert main._valid_access_cookie(token, "secret", 86400)
    assert not main._valid_access_cookie(token, "wrong-secret", 86400)

    monkeypatch.setattr(main.time, "time", lambda: 87_401)
    assert not main._valid_access_cookie(token, "secret", 86400)


def test_access_cookie_rejects_future_issue_time(monkeypatch):
    monkeypatch.setattr(main.time, "time", lambda: 1_000)
    token = f"1001.{main._access_signature('1001', 'secret')}"

    assert not main._valid_access_cookie(token, "secret", 86400)


def test_robots_disallows_all_crawlers():
    response = main.robots()

    assert response.body == b"User-agent: *\nDisallow: /\n"
    assert response.headers["x-robots-tag"] == "noindex, nofollow, noarchive"
