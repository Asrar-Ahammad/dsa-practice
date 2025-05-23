from typing import List


def search_rotated_sorted_arr(arr: List[int], x: int) -> bool:
    n = len(arr)
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == x:
            return True

        # * Searching Left sorted array.
        if arr[mid] > x:
            if arr[low] <= x < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        # * Searching Right sorted array.
        else:
            if arr[mid] < x <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1

    return False


arr = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6]
k = 5

print(search_rotated_sorted_arr(arr, k))
