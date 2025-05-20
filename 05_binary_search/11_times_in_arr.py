from typing import List
import sys

def total_rotations(arr: List[int]):
    n = len(arr)
    low = 0
    high = n - 1
    ans = sys.maxsize
    index = -1

    while low <= high:
        mid = (low+high)//2

        if arr[low] <= arr[mid]:
            if arr[low] < ans:
                index = low
                ans = arr[low]
            low = mid + 1
        else:
            if arr[mid] < ans:
                index = mid
                ans = arr[mid]
            index = mid
            high = mid - 1
    return index, ans

arr = [3,4,5,1,2]
print(f'Total rotation of {arr} are {total_rotations(arr)}')
