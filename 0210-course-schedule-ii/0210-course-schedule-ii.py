class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        res = []

        for edge in prerequisites:
            graph[edge[1]].append(edge[0])
            indegree[edge[0]] += 1

        queue = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
        
        while queue:
            leng = len(queue)

            for _ in range(leng):
                node = queue.pop()
                res.append(node)

                for nebr in graph[node]:
                    indegree[nebr] -= 1

                    if indegree[nebr] == 0:
                        queue.append(nebr)
        
        if len(res) != numCourses:
            return []
        return res


        