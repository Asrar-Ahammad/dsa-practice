import math


def total_tima(arr, h):
    low = 1
    high = max(arr)

    while low <= high:
        sum = 0
        mid = (low + high) // 2

        for i in arr:
            sum += math.ceil(i / mid)

        if sum == h:
            return mid
        elif sum > h:
            low = mid + 1
        else:
            high = mid - 1

    return None


arr = [25, 12, 8, 14, 19]
h = 5

print(total_tima(arr, h))
