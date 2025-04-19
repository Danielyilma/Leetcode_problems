class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        res = [-1] * n
        graph = defaultdict(list)

        for fro, to in redEdges:
            graph[fro].append((to, 0))

        for fro, to in blueEdges:
            graph[fro].append((to, 1))


        queue = deque([(0, 0), (0, 1)])
        visited = set()
        level = 0

        while queue:
            leng = len(queue)

            for _ in range(leng):
                node, color = queue.popleft()

                if res[node] == -1:
                    res[node] = level
                
                for nebr in graph[node]:   
                    edge = (node, nebr[0], 1 - color)                
                    if edge not in visited and nebr[1] != color:
                        queue.append(nebr)
                        visited.add(edge)

            level += 1
        return res