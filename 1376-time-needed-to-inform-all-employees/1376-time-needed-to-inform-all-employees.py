class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)

        for i in range(len(manager)):
            graph[manager[i]].append(i)
        
        def dfs(node):
            time = 0

            for nebr in graph[node]:
                time = max(time, dfs(nebr))
            
            return time + informTime[node]

        return dfs(headID)