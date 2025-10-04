class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        isbound = lambda row, col: 0 <= row < len(board) and 0 <= col < len(board[0])
        res = False
        visited = set()

        def dfs(idx, row, col):
            if idx == len(word) - 1:
                return True

            for r, c in directions:
                new_row, new_col = row + r, col + c

                if not isbound(new_row, new_col):
                    continue
                
                if (new_row, new_col) not in visited and board[new_row][new_col] == word[idx + 1]:
                    visited.add((new_row, new_col))
                    if dfs(idx + 1, new_row, new_col):
                        return True
                    visited.remove((new_row, new_col))
                    
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0] == board[i][j]:
                    visited.add((i, j))
                    if dfs(0, i, j):
                        return True
                    visited.remove((i, j))
        return False



