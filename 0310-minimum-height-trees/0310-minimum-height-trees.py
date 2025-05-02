class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * n
        visited = [0] * n
        res = [0]
        level = 0

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            indegree[v] += 1
            indegree[u] += 1
        
        queue = deque()

        for i in range(n):
            if indegree[i] == 1:
                queue.append(i)

        while queue:
            leng = len(queue)
            temp = []
    

            for _ in range(leng):
                node = queue.popleft()

                temp.append(node)
                visited[node] = 1
                for nebr in graph[node]:
                    indegree[nebr] -= 1

                    if indegree[nebr] == 1 and not visited[nebr]:
                        queue.append(nebr)
            
            level += 1
            res = temp
        
        return res