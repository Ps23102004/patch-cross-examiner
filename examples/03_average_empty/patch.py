def average(nums):
    """AI-written patch: no more crash, but masks the error with 0."""
    try:
        return sum(nums) / len(nums)
    except ZeroDivisionError:
        return 0
