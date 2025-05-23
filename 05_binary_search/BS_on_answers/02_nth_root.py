def nth_root(n: int, m: int) -> int:
    low = 1
    high = m
    ans = -1

    while low <= high:
        mid = (low + high) // 2

        if n ** mid == m:
            ans = mid
            break
        elif n ** mid < m:
            low = mid + 1
        else:
            high = mid - 1

    return ans


n = 3
m = 27
print(f'{n}th root of {m} is {nth_root(n, m)}')
