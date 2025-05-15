class lower_bound:
    def solution(self, arr, target):
        n  = len(arr)
        high = n - 1
        low = 0
        ans = n

        while low <= high:
            mid = (low+high)//2

            if arr[mid] >= target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

# arr = [1, 2, 8, 10, 10, 12, 19]
# x = 5

# arr = [1, 2, 8, 10, 10, 12, 19]
# x = 11

arr = [3, 5, 8, 15, 19]
x = 9
sol = lower_bound()
print(sol.solution(arr, x))