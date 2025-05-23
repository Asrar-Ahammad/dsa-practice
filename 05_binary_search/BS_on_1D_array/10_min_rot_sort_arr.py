from typing import List
import sys

def min_rotated(nums: List[int]) -> int:
    n = len(nums)
    low = 0
    high = n - 1

    mini = sys.maxsize

    while low <= high:
        mid = (low+high)//2

        if arr[low] <= arr[high]:
            mini = min(arr[low], mini)
            break

        if arr[mid] >= arr[low]:
            mini = min(arr[low], mini)
            low = mid + 1
        else:
            mini = min(mini, arr[mid])
            high = mid - 1

    return mini


arr = [3,4,5,1,2]
print(min_rotated(arr))
