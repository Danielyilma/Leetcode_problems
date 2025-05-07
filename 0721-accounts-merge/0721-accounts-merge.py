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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        u = Union()
        res = []

        for acc in accounts:
            name = acc[0]
            
            if len(acc) == 2:
                u.find((name, acc[1]))
            for i in range(2 , len(acc)):
                u.union((name, acc[i]), (name , acc[i - 1]))
        graph = defaultdict(list)

        for key, val in u.parent.items():
            graph[u.find(key)].append(key[1])


        for key, val in graph.items():
            temp = []
            temp.append(key[0])
            temp.extend(sorted(val))

            res.append(temp)
        
        return res

        
        


        








