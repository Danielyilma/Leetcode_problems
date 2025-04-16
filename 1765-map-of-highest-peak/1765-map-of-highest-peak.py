class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rows = len(isWater)
        cols = len(isWater[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        starts = [(i, j) for i in range(rows) for j in range(cols) if isWater[i][j] == 1]
        isbound = lambda x, y: 0 <= x < len(isWater) and 0 <= y < len(isWater[0])
        visited = set(starts)

        queue = deque(starts)
        i = 0

        while queue:
            n = len(queue)

            for _ in range(n):
                x, y = queue.popleft()
                
                isWater[x][y] = i
                for h, v in directions:
                    n_x = x + h
                    n_y = y + v 
                

                    if isbound(n_x, n_y) and (n_x, n_y) not in visited:
                        visited.add((n_x, n_y))
                        queue.append((n_x, n_y))
            i += 1
        
        return isWater


            