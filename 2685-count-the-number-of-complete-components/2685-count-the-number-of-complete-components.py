class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        visited = [0] * n
        res = 0

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        def dfs(node):
            nonlocal node_count
            nonlocal edge_count

            node_count += 1
            edge_count += len(graph[node])

            for nebr in graph[node]:
                if not visited[nebr]:
                    visited[nebr] = 1
                    dfs(nebr)

        
        for i in range(n):
            node_count = 0
            edge_count = 0
            if not visited[i]:
                visited[i] = 1
                dfs(i)

                com_edge = (node_count * (node_count - 1)) // 2
                if com_edge == edge_count // 2:
                    res += 1

        return res