class Union:

    def __init__(self, size=0):
        self.size = defaultdict(int)
        self.parent = defaultdict(tuple)
    

    def find(self, u):
        if u not in self.parent:
            self.parent[u] = u
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
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        costs = []
        res = 0
        for i in range(len(points)):
            for j in range(len(points)):
                if i == j:
                    continue
                x = points[i][0] - points[j][0]
                y = points[i][1] - points[j][1]
                cost = abs(x) + abs(y)
                costs.append((cost, tuple(points[i]), tuple(points[j])))
        costs.sort()

        u = Union()

        for cost in costs:
            if u.get(cost[1], cost[2]):
                continue
            u.union(cost[1], cost[2])
            res += cost[0]
        
        return res