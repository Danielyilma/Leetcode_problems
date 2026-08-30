class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:  
        """
        [   ["A","B","C","E"],
            ["S","F","E","S"],
            ["A","D","E","E"] 
        ]
        
        visted = ("A", "B", "C", "E", "S", "E1", "E2", "E3")
        "ABCESEEEFS"
        """        
        rows, cols = len(board), len(board[0])
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        isbound = lambda row, col: 0 <= row < rows and 0 <= col < cols
        
        def dfs(row, col, idx):
            if idx >= len(word):
                return True
            
            for r, c in directions:
                new_row, new_col = row + r, col + c
                
                if not isbound(new_row, new_col) or (new_row, new_col) in visited:
                    continue
                
                if board[new_row][new_col] == word[idx]:
                    visited.add((new_row, new_col))
                    if dfs(new_row, new_col, idx + 1):
                        return True
                    visited.remove((new_row, new_col))
            
            return False
        
        for i in range(rows):
            for j in range(cols):
                visited = set()
                if board[i][j] == word[0]:
                    visited.add((i, j))
                    if dfs(i, j, 1):
                        return True
                    visited.remove((i, j))
    
   
        return False

            