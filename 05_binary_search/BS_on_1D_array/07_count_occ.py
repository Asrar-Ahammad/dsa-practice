class Solution:
    def last(self, arr, x):
        n = len(arr)
        low = 0
        high = n -1
        last = 0

        while low <= high:
            mid = (low+high)//2

            if arr[mid] <= x:
                last = mid
                low = mid + 1
            elif arr[mid] < x:
                low = mid + 1
            else:
                high = mid - 1
        return last

    
    def first(self, arr, x):
        n = len(arr)
        low = 0
        high = n -1
        first = 0

        while low<= high:
            mid = (low+high)//2

            if arr[mid]==x:
                first = mid
                high = mid - 1
            elif arr[mid] < x:
                low = mid + 1
            else:
                high = mid - 1

        return first

    def count_occurances(self, arr, x):

        first = self.first(arr, x)
        last = self.last(arr, x)

        total = (last - first) + 1
        return total


arr = [2, 2 , 3 , 3 , 3 , 3 ,3, 4]
x = 4

sol = Solution()
print(sol.count_occurances(arr, x))