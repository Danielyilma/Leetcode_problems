class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        queue = deque()

        for i in range(len(prerequisites)):
            graph[prerequisites[i][1]].append(prerequisites[i][0])
            indegree[prerequisites[i][0]] += 1

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        leng = len(queue)
        
        for i in range(leng):
            
            while queue:
                value = queue.popleft()
            
                for nebr in graph[value]:
                    indegree[nebr] -= 1

                    if indegree[nebr] == 0:
                        queue.append(nebr)

        return sum(indegree) == 0
        
