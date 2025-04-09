class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        res = []

        for i, eq in enumerate(equations):
            graph[eq[0]].append((eq[1], values[i]))
            graph[eq[1]].append((eq[0], 1 / values[i]))

        def dfs(node, destin):
            nonlocal total
            visited.add(node)

            if not graph[node]:
                return False

            if node == destin:
                return True


            for neighbour in graph[node]:
                if neighbour[0] in visited:
                    continue
                total *= neighbour[1]
                if dfs(neighbour[0], destin):
                    return True
                total /= neighbour[1]
            return False
    
        
        for query in queries:
            total = 1
            visited = set()
            
            if dfs(query[0], query[1]):
                res.append(total)
            else:
                res.append(-1)
        return res