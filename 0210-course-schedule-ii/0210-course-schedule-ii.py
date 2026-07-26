class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        res = []

        for course, preq in prerequisites:
            graph[course].append(preq)
            indegree[preq] += 1
        
        queue = deque()

        for idx, val in enumerate(indegree):
            if val == 0:
                queue.append(idx) 
        
        while queue:
            value = queue.popleft()
            res.append(value)

            for nebr in graph[value]:
                indegree[nebr] -= 1

                if indegree[nebr] == 0:
                    queue.append(nebr)
        
        return res[::-1] if sum(indegree) == 0 else []
        
