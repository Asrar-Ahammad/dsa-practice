import math

def smallest_divisor(arr, limit):
    n = len(arr)

    if n > limit:
        return -1

    low = 1
    high = max(arr)
    ans = 0

    while low <= high:
        mid = (low + high) // 2

        sum = 0
        for i in arr:
            sum += (int(math.ceil(i / mid)))

        if sum > limit:
            low = mid + 1
        elif sum <= limit:
            high = mid - 1
            ans = mid

    return ans


arr: list[int] = [1, 2, 3, 4, 5]
limit = 8
print(smallest_divisor(arr, limit))
