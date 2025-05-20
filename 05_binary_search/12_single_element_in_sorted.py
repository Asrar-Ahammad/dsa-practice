from collections import Counter


def brute_force(nums):
    freq = Counter(nums)

    for i in freq:
        if freq[i] == 1:
            return i
    return -1


def brute_force_xor(nums):
    ans = 0

    for i in nums:
        ans ^= i
    return ans


def single_element(nums):
    n = len(nums)

    if n == 1: return arr[0]
    if arr[0] != arr[1]: return arr[0]
    if arr[n - 1] != arr[n - 2]: return arr[n - 1]

    low = 1
    high = n - 2

    while low <= high:
        mid = (low + high) // 2

        if arr[mid - 1] != arr[mid] != arr[mid + 1]:
            return arr[mid]
        elif arr[mid - 1] == arr[mid] != arr[mid + 1]:
            low = mid + 1
        else:
            high = mid - 1
    return None


arr = [1, 1, 2, 3, 3, 4, 4, 5, 5, 6, 6]
print(f'The single element in {arr} is {brute_force(arr)}')
print(f'The single element in {arr} is {brute_force_xor(arr)}')
print(f'The single element in {arr} is {single_element(arr)}')
