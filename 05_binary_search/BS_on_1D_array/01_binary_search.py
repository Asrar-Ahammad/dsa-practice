class Solution:
    def binary_search(self, arr, target):
        arr.sort()
        n = len(arr)
        low = 0
        high = n - 1

        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return -1


sol = Solution()
arr = [12, 23, 112, 2, 4, 1, 3, 89, 34, 24, 16]
target = 12
print(f'The target value {target} is at index {sol.binary_search(arr, target)}.')
