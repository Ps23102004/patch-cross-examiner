from candidate import first_index


def test_single_element_found():
    assert first_index([5], 5) == 0


def test_middle_unique():
    assert first_index([1, 2, 3, 4, 5], 3) == 2


def test_absent():
    assert first_index([1, 3, 5], 2) == -1


def test_empty():
    assert first_index([], 1) == -1
