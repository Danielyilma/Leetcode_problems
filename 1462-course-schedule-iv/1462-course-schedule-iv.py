class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        preq_mat = defaultdict(set)
        visited = [0] * numCourses
        res = []

        for pre, course in prerequisites:
            graph[course].append(pre)

        def dfs(node):
            visited[node] = 1
            preq = set()

            for nebr in graph[node]:
                if not visited[nebr]:
                    preq |= dfs(nebr)
                else:
                    preq |= preq_mat[nebr]
                    preq.add(nebr)
    
            preq_mat[node] |= preq
            preq.add(node)

            return preq
        
        for course in range(numCourses):
            if not visited[course]:
                dfs(course)
        
        for query in queries:
            if query[0] in preq_mat[query[1]]:
                res.append(True)
            else:
                res.append(False)
        
        return res
            
                    

