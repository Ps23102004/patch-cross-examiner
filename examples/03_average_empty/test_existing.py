from candidate import average


def test_basic():
    assert average([1, 2, 3]) == 2


def test_single():
    assert average([5]) == 5


def test_float():
    assert average([2, 4]) == 3
