# Todo: Do this question using binary search
def brute_force(arr, k):
    ans = 0
    count = 0
    i = 1
    while count < k:
        if i not in arr:
            ans = i
            count += 1
        i += 1

    return ans
