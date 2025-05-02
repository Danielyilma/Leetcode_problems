class Union:

    def __init__(self, size):
        self.size = [1] * size
        self.parent = [i for i in range(size)]
    

    def find(self, u):

        if self.parent[u] == u:
            return u
        
        self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    

    def union(self, u, v):
        p1 = self.find(u)
        p2 = self.find(v)

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
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        u = Union(n)

        for edge in edges:
            if u.get(edge[0] - 1, edge[1] - 1):
                return edge
            else:
                u.union(edge[0] - 1, edge[1] - 1)

