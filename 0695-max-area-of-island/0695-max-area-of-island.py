class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        is_bound = lambda x, y: 0 <= x < row and 0 <= y < col
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        res = 0

        def dfs(x, y):
            area = 0
            grid[x][y] = 0

            for di in directions:
                n_x = x +  di[0]
                n_y = y + di[1]
                if is_bound(n_x, n_y) and grid[n_x][n_y]:
                    area += dfs(n_x, n_y)
            
            return area + 1


        for i in range(row):
            for j in range(col):
                if grid[i][j]:
                    area = dfs(i, j)
                    res = max(res, area)
        
        return res