def average(nums):
    """Buggy original: ZeroDivisionError on empty input."""
    return sum(nums) / len(nums)
