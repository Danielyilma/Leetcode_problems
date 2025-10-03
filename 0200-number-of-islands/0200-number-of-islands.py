class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        inbound = lambda x, y: 0 <= x < len(grid) and 0 <= y < len(grid[0])
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        visited = set()
        no_islands = 0

        def dfs(row, col):

            for r, c in directions:
                n_row, n_col = row + r, col + c

                if not inbound(n_row, n_col):
                    continue
                
                if (n_row, n_col) not in visited and grid[n_row][n_col] == "1":
                    visited.add((n_row, n_col))
                    dfs(n_row, n_col)                
            
            return
        

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] == "1":
                    visited.add((i, j))
                    dfs(i, j)
                    no_islands += 1
        
        return no_islands