import sys


def brute_force(arr):
    n = len(arr)

    if n == 1: return 0
    if arr[0] > arr[1]: return 0
    if arr[n - 1] > arr[n - 2]: return n - 1

    i = 1
    while i < n - 1:
        if arr[i - 1] < arr[i] > arr[i + 1]:
            return i
        i += 1
    return None


def peak_element(arr):
    n = len(arr)

    if n == 1: return 0
    if arr[0] > arr[1]: return 0
    if arr[n - 1] > arr[n - 2]: return n - 1

    low = 1
    high = n - 2

    while low <= high:
        mid = (low + high) // 2

        if arr[mid - 1] < arr[mid] > arr[mid + 1]:
            return mid
        elif arr[mid - 1] < arr[mid] < arr[mid + 1]:
            low = mid + 1
        else:
            high = mid - 1
    return None


arr = [5, 4, 3, 2, 1]
print(f'The peak element in {arr} is at index {peak_element(arr)}.')
