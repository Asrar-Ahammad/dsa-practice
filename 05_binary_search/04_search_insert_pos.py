class Solution:
    def search_insert_pos(self, arr, k):
        n = len(arr)
        low = 0
        high = n - 1
        ans = n

        while low <= high:
            mid = (low+high)//2

            if arr[mid] >= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
        

arr = [1,2,4,7]
x = 6

sol = Solution()
print(sol.search_insert_pos(arr, x))