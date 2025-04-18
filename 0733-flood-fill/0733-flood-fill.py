class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        visited = [[0] * cols for _ in range(rows)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        queue = deque([(sr, sc)])
        orig = image[sr][sc]
        inbound = lambda row, col: 0 <= row < rows and 0 <= col < cols

        while queue:
            leng = len(queue)

            for _ in range(leng):
                row, col = queue.popleft()
                image[row][col] = color

                for r, c in directions:
                    n_r = row + r
                    n_c = col + c

                    if not inbound(n_r, n_c):
                        continue
                    
                    if image[n_r][n_c] == orig and not visited[n_r][n_c]:
                        visited[n_r][n_c] = 1
                        queue.append((n_r, n_c))
        
        return image
            