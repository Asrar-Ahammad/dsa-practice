class upperbound:
    def optimal(self, arr, k) -> int:
        n = len(arr)
        low = 0
        high = n - 1
        ans = n

        while low <= high:
            mid = (low+high)//2

            if arr[mid] > k:
                ans = mid
                high = mid - 1
            else:
                low = mid +1
        return ans

sol = upperbound()

arr = [3, 5, 8, 15, 19]
k = 9
print(sol.optimal(arr, k))