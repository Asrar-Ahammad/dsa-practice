class Solution:
    def last_occurance(self, arr, x):
        n = len(arr)
        high = n - 1
        low = 0
        ans = -1

        while low<=high:
            mid = (low+high)//2

            if arr[mid] <= x:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
    
    def first(self, arr, x):
        n = len(arr)
        low = 0
        high = n - 1
        first = -1

        while low<=high:
            mid = (low+high)//2

            if arr[mid] >= x:
                first = mid
                high = mid - 1
            elif arr[mid] < x:
                low = mid + 1
            else:
                high = mid - 1
        return first
    
    def first_last(self, arr, x):
        first = self.first(arr, x)
        last = self.last_occurance(arr, x)

        return first, last
    
arr = [3,4,4,13,13,13,20,40]
target = 4

sol = Solution()
print(sol.first_last(arr, target))
