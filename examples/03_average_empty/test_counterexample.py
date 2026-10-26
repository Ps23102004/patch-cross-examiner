import pytest

from candidate import average


def test_empty_raises_value_error():
    # Spec requires ValueError; returning 0 hides the contract violation.
    with pytest.raises(ValueError, match="cannot average empty list"):
        average([])
