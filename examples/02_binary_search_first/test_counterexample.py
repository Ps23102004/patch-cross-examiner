from candidate import first_index


def test_first_of_duplicates():
    # Spec wants the FIRST occurrence; any-match returns 2 here.
    assert first_index([1, 2, 2, 2, 3], 2) == 1


def test_first_of_duplicates_at_start():
    assert first_index([2, 2, 3, 4], 2) == 0
