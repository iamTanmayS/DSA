import math
def nthRoot(n, m):
    l = 1
    h = m
    while l < h:
        mid = (l + h) // 2
        power = abs(math.pow(mid, n))
        if power == m:
            return mid
        elif power < m:
            l = mid + 1  # Fixed logic for updating the lower bound
        else:
            h = mid - 1  # Fixed logic for updating the upper bound
    return -1
