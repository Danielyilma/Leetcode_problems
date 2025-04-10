class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(set)
        visited = set()
        count = 0
        row, col = len(isConnected), len(isConnected[0])

        for i in range(row):
            for j in range(col):
                if not isConnected[i][j]:
                    continue
                graph[i].add(j)
                graph[j].add(i)
            
        
        def dfs(node):

            for neighbour in graph[node]:
                if neighbour in visited:
                    continue
                visited.add(neighbour)
                dfs(neighbour)
        
        for i in  range(len(isConnected)):
            if i not in visited:
                visited.add(i)
                dfs(i)
                count += 1
        
        return count
