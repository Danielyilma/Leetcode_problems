class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        starts = [(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 2]
        isbound = lambda x, y: 0 <= x < len(grid) and 0 <= y < len(grid[0])
        visited = set(starts)
        queue = deque(starts)
        level = -1 if starts else 0
        isrotten = True

        while queue:
            leng = len(queue)

            for _ in range(leng):
                x, y = queue.popleft()
                for h, v in directions:
                    n_x, n_y = x + h, y + v

                    if (n_x, n_y) in visited:
                        continue

                    if isbound(n_x, n_y) and grid[n_x][n_y]:
                        visited.add((n_x, n_y))
                        queue.append((n_x, n_y))
                        grid[n_x][n_y] = 2
            level += 1


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    isrotten = False
                    break
        
        if not isrotten:
            return -1
        
        return level