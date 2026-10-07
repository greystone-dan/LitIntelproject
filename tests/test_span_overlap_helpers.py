import random

from backend.citations import _GrowingSpanSet, _span_overlap_checker


def _brute(spans, start, end):
    return any(not (end <= s or start >= e) for s, e in spans)


def test_span_overlap_checker_matches_a_full_scan():
    rng = random.Random(7)
    for _ in range(300):
        spans = []
        for _ in range(rng.randint(0, 12)):
            s = rng.randint(0, 40)
            spans.append((s, s + rng.randint(0, 8)))
        check = _span_overlap_checker(spans)
        for _ in range(30):
            a = rng.randint(0, 50)
            b = a + rng.randint(0, 10)
            assert check(a, b) == _brute(spans, a, b)


def test_growing_span_set_matches_a_full_scan_when_only_free_spans_are_kept():
    rng = random.Random(11)
    for _ in range(300):
        kept = []
        growing = _GrowingSpanSet()
        for _ in range(25):
            a = rng.randint(0, 60)
            b = a + rng.randint(0, 9)
            expected = _brute(kept, a, b)
            assert growing.overlaps(a, b) == expected
            if not expected:
                kept.append((a, b))
                growing.add(a, b)
