class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        ancestor = defaultdict(set)
        res = []
        parents = set(list(range(n)))

        for edge in edges:
            graph[edge[1]].append(edge[0])
            parents.discard(edge[0])


        def dfs(node):
            childs = []

            for nebr in graph[node]:
                if not visited[nebr]:
                    visited[nebr] = 1
                    childs.extend(dfs(nebr))
                else:
                    childs.append(nebr)
                    childs.extend(ancestor[nebr])

            ancestor[node].update(childs)
            childs.append(node)

            return childs


        for parent in parents:
            visited = [0] * n
            dfs(parent)


        for node in range(n):
            res.append(sorted(ancestor[node]))
        

        return res
