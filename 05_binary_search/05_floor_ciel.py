class Solutions:
    def ciel(self, arr, x):
        n = len(arr)
        high = n - 1
        low = 0
        ans = -1

        while low<=high:
            mid = (low+high)//2

            if arr[mid]>= x:
                ans = arr[mid]
                high = mid - 1
            else:
                low = mid + 1
        return ans
    
    def floor(self, arr, x):
        n = len(arr)
        high = n - 1
        low = 0
        ans = -1

        while low <= high:
            mid = (low+high)//2

            if arr[mid] <= x:
                ans = arr[mid]
                low = mid + 1
            else:
                high = mid - 1
        return ans

    def floor_ciel(self, arr, x):
        ciel_num = self.ciel(arr, x)
        floor_num = self.floor(arr, x)

        return floor_num, ciel_num


arr = [3, 4, 4, 7, 8, 10]
x = 5

sol = Solutions()
print(sol.floor_ciel(arr, x))
