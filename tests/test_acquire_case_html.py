from scripts.acquire_case_html import HostLimiter


def test_host_limiter_rejects_negative_delay():
    try:
        HostLimiter(-1)
    except ValueError:
        pass
    else:
        raise AssertionError("negative per-host delay must fail")


def test_host_limiter_accepts_polite_defaults():
    limiter = HostLimiter(2.0)
    limiter.wait("example.test")
    assert limiter.interval_seconds == 2.0
