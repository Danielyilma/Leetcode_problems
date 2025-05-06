
class Union:

    def __init__(self, size):
        self.size = [1] * (26 + 1)
        self.parent = [i for i in range(26 + 1)]
    

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
    def equationsPossible(self, equations: List[str]) -> bool:
        n = set()

        for eq in equations:
            n.add(eq[0])
            n.add(eq[-1])
        
        u = Union(len(eq))
        neg = []

        for eq in equations:
            a = ord(eq[0]) - ord("a")
            b = ord(eq[-1]) - ord("a")
            if eq[1:3] == "==":
                u.union(a, b)
            else:
                neg.append((a, b))

        for a, b in neg:
            if u.get(a, b):
                return False
        
        return True