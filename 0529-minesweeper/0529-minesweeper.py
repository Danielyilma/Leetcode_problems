class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        rows, cols = len(board), len(board[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        isbound = lambda row, col: 0 <= row < rows and 0 <= col < cols
        queue = deque([click])
        visited = set()
        res = copy.deepcopy(board)
        
        while queue:
            new_queue = []
            row, col = queue.popleft()
            count = 0

            if board[row][col] == "M":
                res[row][col] = "X"
                break

            for r, c in directions:
                n_r, n_c = row + r, col + c

                if isbound(n_r, n_c) and (n_r, n_c) not in visited:
                    if board[n_r][n_c] == "M":
                        count += 1
                    new_queue.append((n_r, n_c))

            if count == 0:
                res[row][col] = "B"
                visited.update(new_queue)
                queue.extend(new_queue)
            else:
                res[row][col] = str(count)

        return res
                