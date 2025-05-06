class Union:

    def __init__(self, size=0):
        self.size = {}
        self.parent = {}

        for i in range(size):
            for j in range(size):
                for k in range(4):
                    self.size[(i, j, k)] = 1
                    self.parent[(i, j, k)] = (i, j, k)
        print(self.parent)

    def find(self, u):
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
    def regionsBySlashes(self, grid: List[str]) -> int:
        u = Union(len(grid))
        res = 0
        
        for i in range(len(grid)):
            j = 0
            while j < len(grid):
                
                if grid[i][j] == "\\":
                    u.union((i, j, 0), (i, j, 1))
                    u.union((i, j, 2), (i, j, 3))
                elif grid[i][j] == " ":
                    u.union((i, j, 0), (i, j, 1))
                    u.union((i, j, 2), (i, j, 3))
                    u.union((i, j, 0), (i, j, 2))
                else:
                    u.union((i, j, 0), (i, j, 2))
                    u.union((i, j, 1), (i, j, 3))
                
                if i - 1 >= 0:
                    u.union((i, j, 0), (i - 1, j, 3))
                
                if j - 1 >= 0:
                    u.union((i, j, 2), (i, j - 1, 1))

                j += 1

        for key, val in u.parent.items():
            if key == val:
                res += 1
        return res

                    






















        