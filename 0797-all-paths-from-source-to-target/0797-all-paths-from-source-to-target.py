class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []

        def dfs(node, dest, path):
            if node == dest:
                paths.append(path[::])
                return
            
            for nebr in graph[node]:
                path.append(nebr)
                dfs(nebr, dest, path)
                path.pop()
        
        dfs(0, len(graph) - 1, [0])
        return paths

            

            
