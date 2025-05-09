class Union:

    def __init__(self, size=0):
        self.size = defaultdict(int)
        self.parent = defaultdict(tuple)
        self.min = defaultdict(int)
    

    def find(self, u):
        if u not in self.parent:
            self.parent[u] = u
            self.size[u] = 1
            self.min[u] = ord(u)
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
            self.min[p1] = min(self.min[p1], self.min[p2])
            self.size[p1] += self.size[p2]
        else:
            self.parent[p1] = p2
            self.min[p2] = min(self.min[p1], self.min[p2])
            self.size[p2] += self.size[p1]


    def get(self, u, v):
        p1 = self.find(u)
        p2 = self.find(v)

        return p1 == p2


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        res = []
        u = Union()


        for i in range(len(s1)):
            u.union(s1[i], s2[i])
        
        for s in baseStr:
            p1 = u.find(s)
            res.append(chr(u.min[p1]))
        
        return "".join(res)