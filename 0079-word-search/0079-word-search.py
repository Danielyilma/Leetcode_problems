class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        rows, cols = len(board), len(board[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        inbound = lambda row, col: 0 <= row < rows and 0 <= col < cols

        def dfs(row, col, index):
            if index >= len(word):
                return True

            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy

                if not inbound(new_row, new_col) or (new_row, new_col) in visited:
                    continue
                

                if board[new_row][new_col] != word[index]:
                    continue
                
                visited.add((new_row, new_col))
                if dfs(new_row, new_col, index + 1):
                    return True
                visited.remove((new_row, new_col))
            
            return False
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] != word[0]:
                    continue

                visited.add((i, j))
                if dfs(i, j, 1):
                    return True
                visited.remove((i, j))
        
        return False

            
