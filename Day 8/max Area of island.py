class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = []
        def Solve(grid,m,n,i,j):
            if i < 0 or j < 0 or i >= m or j >=n or grid[i][j]==0:
                return 0
            grid[i][j] = 0
            a = Solve(grid,m,n,i+1,j)
            b = Solve(grid,m,n,i-1,j)
            c = Solve(grid,m,n,i,j+1)
            d = Solve(grid,m,n,i,j-1)
            res = 1 + a + b + c + d
            max_area.append(res)
            return res
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    Solve(grid,m,n,i,j)
        if max_area == []:
            return 0
        return max(max_area)