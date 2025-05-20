def rot_sorted_arr_search(nums, target):
    n = len(nums)
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2

        # if midpoints the target
        if arr[mid] == target:
            return mid

        # if left part is sorted
        if arr[low] <= arr[mid]:
            if arr[low] <= target <= arr[mid]:
                # element exists
                high = mid - 1
            else:
                # element does not exist
                low = mid + 1
        else:  # if right part is sorted
            if arr[mid] <= target <= arr[high]:
                # element exists
                low = mid + 1
            else:
                # element does not exist
                high = mid - 1
    return -1


arr = [4, 5, 6, 7, 0, 1, 2, 3]
arr_1 = [4, 5, 6, 7, 8, 1, 2, 3]
arr_2 = [3, 1]
x = 1
print(rot_sorted_arr_search(arr_2, x))
