from candidate import dedup


def test_first_seen_order_preserved():
    # The spec pins order; a set-based "fix" cannot satisfy this.
    assert dedup([3, 1, 3, 2, 1]) == [3, 1, 2]


def test_first_seen_order_strings():
    assert dedup(["b", "a", "b", "c", "a"]) == ["b", "a", "c"]
