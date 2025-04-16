class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        directions = [(0,1), (0, - 1), (1, 0), (-1, 0)]
        rows = len(maze)
        cols = len(maze[0])
        def out_bound(row, col):
            return row < 0 or col < 0 or row >= rows or col >= cols
        
        q = deque([entrance])
        maze[entrance[0]][entrance[1]] = "+"
        ans = 0
        while q:
            ans += 1
            n = len(q)
            for i in range(n):
                row, col = q.popleft()
                
                for x, y in directions:
                    nr = x + row
                    nc = y + col
                    if not out_bound(nr, nc) and maze[nr][nc] == ".":
                        maze[nr][nc] = "+"
                        q.append((nr,nc))
                        if nr == 0 or nc == 0 or nr == rows - 1 or nc == cols - 1:
                            return ans

        return -1