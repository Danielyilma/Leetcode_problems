class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # [
        #   (0, 0), (0, 1), (0, 2)
        #   (1, 0), (1, 1), (1, 2)
        #   (2, 0), (2, 1) (2, 2)
        #]
        
        res = []
        grid = [["."] * n for _ in range(n)]
        isbound = lambda row, col: 0 <= row < n and 0 <= col < n
        row_visited = set()
        col_visited = set()
        dig_visited = set()
        neg_dig_visited = set()
        print(grid)
        
        
        def dfs(row, grid):
            
            if row >= n:
                res.append(["".join(grid[i]) for i in range(n)])
                return
                
            
            for col in range(n):
                neg_sum = row + col
                pos_sum = row - col
                
                if col in col_visited or pos_sum in dig_visited or neg_sum in neg_dig_visited:
                    continue
                
                row_visited.add(row)
                col_visited.add(col)
                dig_visited.add(pos_sum)
                neg_dig_visited.add(neg_sum)
                grid[row][col] = "Q"
                dfs(row + 1, grid)
                grid[row][col] = "."
                row_visited.remove(row)
                col_visited.remove(col)
                dig_visited.remove(pos_sum)
                neg_dig_visited.remove(neg_sum)
            
            return
        
        dfs(0, grid)
        
        return res
    
                
                
                   
            
        
         
        