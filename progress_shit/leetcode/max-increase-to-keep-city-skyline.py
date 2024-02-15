class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res=0

        row_max=[0]*rows
        col_max=[0]*cols

        for i in range(rows):
            for j in range(cols):
                row_max[i]=max(row_max[i], grid[i][j])
                col_max[i]=max(col_max[i], grid[j][i])
        print(row_max, col_max)

        for i in range(rows):
            for j in range(cols):
                res+=(min(row_max[i], col_max[j]) - grid[i][j])
                
        return res

        