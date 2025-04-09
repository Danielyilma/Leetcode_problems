class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        group = [-1] * (n + 1)
        graph = defaultdict(list)

        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node):
            for neighbour in graph[node]:
                if group[neighbour] == -1:
                    group[neighbour] = 1 - group[node]
                    if not dfs(neighbour):
                        return False
                elif group[neighbour] == group[node]:
                        return False
            return True
        

        for i in range(1, n + 1):
            if group[i] == -1:
                group[i] = 0
                if not dfs(i):
                    return False
        return True