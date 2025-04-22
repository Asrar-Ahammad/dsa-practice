from typing import List

class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        step = 0
        prev = grid[0][0]
        i = 1
        j = 0

        while j < len(grid[0]):
            while i < len(grid):
                curr = grid[i][j]

                if curr < prev:
                    diff = (prev - curr) + 1
                    grid[i][j] = curr + diff
                    step = step + diff
                    prev = grid[i][j]
                    i += 1
                elif curr == prev:
                    diff = 1
                    grid[i][j] = curr + diff
                    step = step + diff
                    prev = grid[i][j]
                    i += 1
                else:
                    prev = curr
                    i += 1
            j += 1
            if j < len(grid[0]):
                prev = grid[0][j]
            i = 1
        return step

arr = [[3,2],[1,3],[3,4],[0,1]]

sol = Solution()
print(sol.minimumOperations(arr))