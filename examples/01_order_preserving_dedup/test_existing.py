from candidate import dedup


def test_removes_duplicates():
    assert sorted(dedup([3, 1, 3, 2, 1])) == [1, 2, 3]


def test_empty():
    assert dedup([]) == []


def test_no_duplicates_unchanged_set():
    assert sorted(dedup([5, 4])) == [4, 5]
