class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        Count=0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (grid[i][j]<0):
                    Count+=1
        return Count