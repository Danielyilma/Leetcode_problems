class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        inbound = lambda row, col: 0 <= row < rows and 0 <= col < cols
        starts = [(i,j) for i in range(rows) for j in range(cols) if not mat[i][j]]
        visited = set(starts)
        queue = deque(starts)
        level = 0

        while queue:
            leng = len(queue)

            for _ in range(leng):
                row, col = queue.popleft()
                if mat[row][col] == 1:
                    mat[row][col] = level

                for r, c in directions:
                    n_r = row + r
                    n_c = col + c

                    if inbound(n_r, n_c) and (n_r, n_c) not in visited:
                        visited.add((n_r, n_c))
                        queue.append((n_r, n_c))
            level += 1

        return mat