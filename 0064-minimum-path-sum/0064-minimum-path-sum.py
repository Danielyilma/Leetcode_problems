class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0)]
        destination = (len(grid) - 1, len(grid[0]) - 1)
        store = {}

        isbound = lambda row, col: 0 <= row < len(grid) and 0 <= col < len(grid[0])

        def dfs(row, col):
            nonlocal destination
            sums = float("inf")

            if (row, col) == destination:
                return grid[row][col]

            if (row, col) in store:
                return store[(row, col)]

            for r, c in directions:
                new_row, new_col = row + r, col + c

                if not isbound(new_row, new_col):
                    continue

                count = dfs(new_row, new_col)
                store[(new_row, new_col)] = count
                sums = min(sums, count)
            
            return sums + grid[row][col]
        
        return dfs(0, 0)
                

                
