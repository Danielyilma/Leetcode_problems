class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = [-1] * 100
        
        def bfs(node):
            queue = deque([node])

            while queue:
                leng = len(queue)

                for _ in range(leng):
                    node = queue.popleft()

                    for nebr in graph[node]:
                        if colors[nebr] == colors[node]:
                            return False
                        elif colors[nebr] == -1:
                            colors[nebr] = 1 - colors[node]
                            queue.append(nebr)
                
            return True
        
        for i in range(len(graph)):
            if colors[i] == -1:
                colors[i] = 0
                if not bfs(i):
                    return False
        
        return True
