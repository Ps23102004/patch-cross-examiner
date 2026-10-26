def first_index(a, target):
    lo, hi = 0, len(a) - 1
    result = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == target:
            result = mid
            hi = mid - 1  # keep searching left for the first occurrence
        elif a[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return result
