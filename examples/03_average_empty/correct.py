def average(nums):
    if not nums:
        raise ValueError("cannot average empty list")
    return sum(nums) / len(nums)
