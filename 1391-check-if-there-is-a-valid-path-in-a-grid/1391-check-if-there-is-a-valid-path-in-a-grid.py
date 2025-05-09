class Union:

    def __init__(self, size=0):
        self.size = defaultdict(int)
        self.parent = defaultdict(tuple)
    

    def find(self, u):
        if u not in self.parent:
            self.parent[u] = u
            self.size[u] = 1
            return u

        if self.parent[u] == u:
            return u
        
        self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    

    def union(self, u, v):
        p1 = self.find(u)
        p2 = self.find(v)

        if p1 == p2:
            return

        if self.size[p1] > self.size[p2]:
            self.parent[p2] = p1
            self.size[p1] += self.size[p2]
        else:
            self.parent[p1] = p2
            self.size[p2] += self.size[p1]


    def get(self, u, v):
        p1 = self.find(u)
        p2 = self.find(v)

        return p1 == p2


class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        directions = {
            1: {(0, -1), (0, 1)},
            2: {(-1, 0), (1, 0)},
            3: {(0, -1), (1, 0)},
            4: {(0, 1), (1, 0)},
            5: {(0, -1), (-1, 0)},
            6: {(0, 1), (-1, 0)}
        }
        u = Union()
        start = (0, 0)
        end = (len(grid) - 1, len(grid[0]) - 1)
        isbound = lambda row, col: 0 <= row < len(grid) and 0 <= col < len(grid[0])


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                for r, c in directions[grid[i][j]]:
                    n_r, n_c = i + r, j + c

                    if isbound(n_r, n_c) and (-1 * r, -1 * c) in directions[grid[n_r][n_c]]:
                        u.union((i, j), (n_r, n_c))
        
        return u.get(start, end)

    
