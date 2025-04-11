class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])
        visited = set()

        is_bound = lambda x, y: 0 <= x < row and 0 <= y < col
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        res = 0

        def dfs(x, y):
            board[x][y] = "Y"

            for di in directions:
                n_x = x + di[0]
                n_y = y + di[1]

                if is_bound(n_x, n_y) and board[n_x][n_y] == "O":
                    dfs(n_x, n_y)



        for i in (0, row - 1):
            for j in range(col):
                if board[i][j] == "O":
                    dfs(i, j)
        
        for i in (0, col - 1):
            for j in range(row):
                if board[j][i] == "O":
                    dfs(j, i)
        
        for i in range(row):
            for j in range(col):
                if board[i][j] == "Y":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"
        

            
