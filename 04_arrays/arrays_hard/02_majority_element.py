import collections

class Solution:
    def majority_element(self, arr):
        n = len(arr)
        res = []
        freq = collections.Counter(arr)

        for i in freq:
            if freq[i] > n//3:
                res.append(i)

        return res

arr = [11,33,33,11,33,11]
sol = Solution()
print(sol.majority_element(arr))