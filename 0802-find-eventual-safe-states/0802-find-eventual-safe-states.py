class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        indegree = defaultdict(int)
        graphs = defaultdict(list)
        res = []

        for i, nebrs in enumerate(graph):
            for node in nebrs:
                graphs[node].append(i)
                indegree[i] += 1
            

        queue = deque()
        for node in range(len(graph)):
            if indegree[node] == 0:
                queue.append(node)
        
        while queue:
            leng = len(queue)

            for _ in range(leng):
                node = queue.pop()
                res.append(node)

                for nebr in graphs[node]:
                    indegree[nebr] -= 1

                    if indegree[nebr] == 0:
                        queue.append(nebr)
        
        
        return sorted(res)


        